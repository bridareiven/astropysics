#Copyright (c) 2008 Erik Tollerud (etolleru@uci.edu) 
"""
This module stores physical constants and conversion factors for the astropysics
package.

Some of the package-level variables are generated from the currently selected
Cosmology (see Cosmology object and choose_cosmology function for details)
"""

from __future__ import division,with_statement
from math import pi
import numpy as np

#<--------------------------------Constants------------------------------------>
#all in cgs including gaussian esu for charge
prop=property(lambda:5)
unit_system='cgs'

G=6.673e-8
mp=1.67262171e-24
me=9.1093897e-28
e=4.8032068e-10
Ms=1.9891e33
Mj=1.8986e30
Me=5.9742e27
Rs=6.96e10
Rj=7.1492e9
Re=6.371e8
Lsun=3.839e33
De=1.49597887e13
kb=1.3807e-16 
#sigma=5.6704e-5
c=2.99792458e10 #exact
h=6.626068E-27

#<-------------------------------Conversions----------------------------------->
ergperev=1.60217646e-12
secperday=86400 #IAU standard
secperyr=365.25*secperday#3.15576926e7
secpergyr=secperyr*1e9
cmperpc=3.08568025e18
pcpercm=1.0/cmperpc
lyperpc=3.26
pcperly=1.0/lyperpc
cmperau=1.49598e13
aupercm=1.0/cmperau


#TODO:rethink flux units and adapt to BlackbodyModel
def flambda_to_fnu_l(flambda,lamb):
    return flambda*lamb*lamb/c

def fnu_to_flambda_l(fnu,lamb):
    return fnu*c/lamb/lamb

def flambda_to_fnu_n(flambda,nu):
    return flambda*c/nu/nu

def fnu_to_flambda_n(fnu,nu):
    return fnu*nu*nu/c


#<--------------------------------Cosmology------------------------------------>
class Cosmology(object):
    """
    This class represents a cosmology and should be subclassed
    
    all cosmologies should have a hubble constant (H0) in km/s/Mpc
    
    while not required
    
    Cosmologies should also include a sequence called "_params_" with a list of
    strings that specify the names of the cosmological parameters associated to
    be exported to the constants module
    """
    #TODO:use ABCs in py 2.6
    _params_=('H0',)
    
    H0=0
    
    def __init__(self,*args,**kwargs):
        ps=self._params_
    h = property(lambda self:self.H0/100.0)
    h7 = h70 = property(lambda self:self.H0/70.0)
    __params_cache=None
    def _getParams(self):
        if self.__params_cache is None:
            import inspect
            pars= [cls._params_ for cls in inspect.getmro(self.__class__) if 
                    hasattr(cls,'_params_')]
            s=set()
            for p in pars:
                s.update(p)
            self.__params_cache = tuple(s)
        return self.__params_cache
    params=property(_getParams)
    
    def _exportParams(self):
        pd=dict([(p,getattr(self,p)) for p in self.params])
        globals().update(pd)
        
    def _removeParams(self):
        from warnings import warn
        d=globals()
        for p in self.params:
            out=d.pop(p,None)
            if out is None:
                warn('Cosmological parameter %s not present despite being current cosmology'%p)
        
    
    
class FRWCosmology(Cosmology):
    """
    A cosmology based on the FRW metric  with a global density, a matter 
    density, and a radiation density, and a comological constant as 
    specified at z=0
    
    default values are approximately LambdaCDM
    """
    _params_=('omega','omegaR','omegaM','omegaL')
    
    H0=72
    omega = property(lambda self:self.omegaR+self.omegaM+self.omegaL)
    omegaR=0 #radiation density
    omegaM=0.3 #matter density
    omegaL=0.7 #dark energy density
    
    @property
    def omegaK(self):
        return 1-self.omegaR-self.omegaM-self.omegaL
    
    def H(self,z):
        z=np.array(z)
        M,L,R=self.omegaM,self.omegaL,self.omegaR
        K=1-M-L-R
        a=1/(1+z)
        return self.H0*(R*a**-4 + M*a**-3 + L + K*a**-2)**0.5
        
    def computeOmegaRz(self,z):
        """
        compute radiation density at arbitrary redshift
        """
        a=1/(1+z)
        return (self.rhoC(0)/self.rhoC(z))*self.omegaR*a**-4
        
    def computeOmegaMz(self,z):
        """
        compute matter density at arbitrary redshift
        """
        a=1/(1+z)
        return (self.rhoC(0)/self.rhoC(z))*self.omegaM*a**-3
    
    def computeOmegaLz(self,z):
        """
        compute cosmological constant density at arbitrary redshift
        """
        return self.omegaL*(self.rhoC(0)/self.rhoC(z))
    
    def computeOmegaKz(self,z,units='cgs'):
        """
        compute curvature density at arbitrary redshift
        """
        a=1/(1+z)
        return (self.rhoC(0)/self.rhoC(z))*self.omegaK*a**-2
    
    def rhoC(self,z=0,units='cgs'):
        """
        critical density at a given redshift
        
        units can be 'cgs' or 'cosmological' (Mpc,Msun)
        TODO:check
        """
        H = self.H(z)*1e5*1e-6*pcpercm #km/s->cm/s, Mpc->cm
        cgsres = 3*H*H/(8*pi*G)
        
        if units == 'cgs':
            return cgsres
        elif units == 'cosmological':
            return cgsres/Ms*(1e-6*pcpercm)**-3#g->Msun,cm^-3->Mpc^-3
        else:
            raise ValueError('unrecognized units')
        
    
    def rho(self,z=0,units='cgs'):
        """
        mean density in this cosmology
        
        units can be 'cgs' or 'cosmological' (Mpc,Msun)
        """
        return self.omega*self.rhoC(z,units)
    
    def deltavir(self,z=0):
        """
        virial overdensity as paramaterized in Bryan&Norman 98 for omega=1
        """
        if self.omegaK !=0:
            raise NotImplementedError("can't compute for omega!=1")
        om = self.computeOmegaMz(z)
        x= om - 1
        return (18*pi**2+82*x-39*x**2)/om

class WMAP7Cosmology(FRWCosmology):
    """
    WMAP7-only (http://lambda.gsfc.nasa.gov/product/map/dr4/params/lcdm_sz_lens_wmap7.cfm)
    """
    _params_ = ('t0','sigma8')
    t0 = 13.71#Gyr
    sigma8 = .801
    H0 = 71.0
    omegaB = 0.044
    omegaC = 0.222
    omegaL = 0.734
    omegaM = property(lambda self:self.omegaB+self.omegaC)
    
class WMAP7BAOH0Cosmology(FRWCosmology):
    """
    WMAP7+BAO+H0 (http://lambda.gsfc.nasa.gov/product/map/dr4/params/lcdm_sz_lens_wmap7_bao_h0.cfm)
    """
    _params_ = ('t0','sigma8')
    t0 = 13.78#Gyr
    sigma8 = 0.809
    H0 = 70.4
    omegaB = 0.045
    omegaC = 0.227
    omegaL = 0.728
    omegaM = property(lambda self:self.omegaB+self.omegaC)
    
class WMAP5Cosmology(FRWCosmology):
    """
    WMAP5-only (http://lambda.gsfc.nasa.gov/product/map/dr3/parameters_summary.cfm)
    """
    _params_=('t0','sigma8')
    t0=13.69 #Gyr
    sigma8=.796
    H0=71.9
    omegaB=0.044
    omegaC=0.214
    omegaL=0.742
    omegaM=property(lambda self:self.omegaB+self.omegaC)
    
class WMAP5BAOSNCosmology(FRWCosmology):
    """
    WMAP5+BAO+SN (http://lambda.gsfc.nasa.gov/product/map/dr3/parameters_summary.cfm)
    """
    _params_=('t0','sigma8')
    t0=13.73 #Gyr
    sigma8=.817
    H0=70.1
    omegaB=0.046
    omegaC=0.233
    omegaL=0.721
    omegaM=property(lambda self:self.omegaB+self.omegaC)
    
class WMAP3Cosmology(FRWCosmology):
    """
    WMAP3 only (http://lambda.gsfc.nasa.gov/product/map/dr2/params/lcdm_wmap.cfm)
    """
    #_params_=('t0','sigma8')
    _params_=('sigma8')
    #t0=13.69 #Gyr
    sigma8=.761
    H0=73.2
    omegaB=0.044
    omegaC=0.224
    omegaL=0.732
    omegaM=property(lambda self:self.omegaB+self.omegaC)
    
class WMAP3AllCosmology(FRWCosmology):
    """
    WMAP3+all (http://lambda.gsfc.nasa.gov/product/map/dr2/params/lcdm_all.cfm)
    """
    #_params_=('t0','sigma8')
    _params_=('sigma8')
    #t0=13.69 #Gyr
    sigma8=.776
    H0=70.4
    omegaB=0.042+.002/3 #omega=1
    omegaC=0.197+.002/3 #omega=1
    omegaL=0.759+.002/3 #omega=1
    omegaM=property(lambda self:self.omegaB+self.omegaC)


__current_cosmology=WMAP7BAOH0Cosmology() #default value
__current_cosmology._exportParams()
__cosmo_registry={}

def register_cosmology(cosmocls,name=None):
    """
    Add the provided subclass of Cosmology to the cosmology registry
    
    if name is None, the name will be inferred from the class name, otherwise
    
    """
    if not name:
        name = cosmocls.__name__
    name = name.lower().replace('cosmology','')
    try:
        if not issubclass(cosmocls,Cosmology):
            raise TypeError("Supplied object is not a subclass of Cosmology")
    except TypeError:
        raise TypeError("Supplied object to register is not a class")
    
    __cosmo_registry[name]=cosmocls
    
#register all Cosmologies in this module
for o in locals().values():
    if type(o)==type and issubclass(o,Cosmology) and o != Cosmology:
        register_cosmology(o)

def choose_cosmology(nameorobj,*args,**kwargs):
    """
    Select the currently active cosmology and export its cosmological 
    parameters into the package namespace
    
    nameorobj can be a string or a Cosmology object
    
    If string, a new instance corresponding to the type with the given name in 
    the cosmology registry is generated with the args and kwargs going into the 
    initializer.
    
    If nameorobj is an instance of Cosmology, the supplied object is selected as 
    the current cosmology and the registry is updated to include its class, if 
    it is not already present
    
    return value is the cosmology object
    """
    global __current_cosmology
    
    if isinstance(nameorobj,basestring):
        c = __cosmo_registry[nameorobj.lower()](*args,**kwargs)
    elif isinstance(nameorobj,Cosmology):
        c = nameorobj
        if c.__class__ not in __cosmo_registry.values():
            register_cosmology(c.__class__)
    
    __current_cosmology._removeParams()
    try:
        c._exportParams()
        __current_cosmology =  c
    except:
        __current_cosmology._exportParams()
        
    return c
    
    
def get_cosmology(name=None):
    """
    if name is None, will retreive the currently in use Cosmology instance.
    Otherwise, returns the Class object for the requested cosmology
    """
    if name is None:
        return __current_cosmology
    else:
        return __cosmo_registry[name]
    
def update_cosmology():
    """
    updates the package-level variables for changes in the current Cosmology 
    object
    """
    __current_cosmology._exportParams()

def get_registry_names():
    """
    Returns the names of all cosmology types in the registry
    """
    return __cosmo_registry.keys()
