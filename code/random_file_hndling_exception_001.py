Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import json
>>> import math
>>> import csv
>>> import random
>>> import matplotlib
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    import matplotlib
ModuleNotFoundError: No module named 'matplotlib'
>>> import random
>>> random.random()
0.835979026771305
>>> random.random()# random is function in random mudule
0.18482712257494327
>>> random.random()# random is function in random mudule
0.524147450331252
>>> random.random()# random is function in random mudule
0.05600790916974285
>>> random.random()# random is function in random mudule.it is used to give random number between 0 and 1
0.38529250237362844
>>> randon.randint(30,90)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    randon.randint(30,90)
NameError: name 'randon' is not defined
>>> random.randint(30,90)
54
>>> random.randint(30,90)
30
>>> random.uniform(10,30)
19.094652477507815
>>> random.uniform(10,30)
28.56721588015366
>>> random.uniform(10,30)#it give floatpoint number between two number
23.11698532599008
>>> random.randint(30,90)#it give int value
47
>>> item=[1,2,3,4,5,6,7,8,9,10]
>>> random.shuffle(item)
>>> item
[5, 4, 10, 2, 3, 9, 8, 6, 7, 1]
>>> random.shuffle(item)#it change the number or mila diya ulta pulta
>>> item
[5, 9, 7, 4, 8, 2, 10, 6, 1, 3]
>>> x=random.sample(item,3)
>>> x
[6, 3, 4]
>>> x=random.sample(item,3)#it provide three any value from list
>>> x
[5, 4, 9]
>>> help(random)
Help on module random:

NAME
    random - Random variable generators.

DESCRIPTION
        integers
        --------
               uniform within range
    
        sequences
        ---------
               pick random element
               pick random sample
               pick weighted random sample
               generate random permutation
    
        distributions on the real line:
        ------------------------------
               uniform
               triangular
               normal (Gaussian)
               lognormal
               negative exponential
               gamma
               beta
               pareto
               Weibull
    
        distributions on the circle (angles 0 to 2pi)
        ---------------------------------------------
               circular uniform
               von Mises
    
    General notes on the underlying Mersenne Twister core generator:
    
    * The period is 2**19937-1.
    * It is one of the most extensively tested generators in existence.
    * The random() method is implemented in C, executes in a single Python step,
      and is, therefore, threadsafe.

CLASSES
    _random.Random(builtins.object)
        Random
            SystemRandom
    
    class Random(_random.Random)
     |  Random number generator base class used by bound module functions.
     |  
     |  Used to instantiate instances of Random to get generators that don't
     |  share state.
     |  
     |  Class Random can also be subclassed if you want to use a different basic
     |  generator of your own devising: in that case, override the following
     |  methods:  random(), seed(), getstate(), and setstate().
     |  Optionally, implement a getrandbits() method so that randrange()
     |  can cover arbitrarily large ranges.
     |  
     |  Method resolution order:
     |      Random
     |      _random.Random
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __getstate__(self)
     |      # Issue 17489: Since __reduce__ was defined to fix #759889 this is no
     |      # longer called; we leave it here because it has been here since random was
     |      # rewritten back in 2001 and why risk breaking something.
     |  
     |  __init__(self, x=None)
     |      Initialize an instance.
     |      
     |      Optional argument x controls seeding, as for Random.seed().
     |  
     |  __reduce__(self)
     |      helper for pickle
     |  
     |  __setstate__(self, state)
     |  
     |  betavariate(self, alpha, beta)
     |      Beta distribution.
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      Returned values range between 0 and 1.
     |  
     |  choice(self, seq)
     |      Choose a random element from a non-empty sequence.
     |  
     |  choices(self, population, weights=None, *, cum_weights=None, k=1)
     |      Return a k sized list of population elements chosen with replacement.
     |      
     |      If the relative weights or cumulative weights are not specified,
     |      the selections are made with equal probability.
     |  
     |  expovariate(self, lambd)
     |      Exponential distribution.
     |      
     |      lambd is 1.0 divided by the desired mean.  It should be
     |      nonzero.  (The parameter would be called "lambda", but that is
     |      a reserved word in Python.)  Returned values range from 0 to
     |      positive infinity if lambd is positive, and from negative
     |      infinity to 0 if lambd is negative.
     |  
     |  gammavariate(self, alpha, beta)
     |      Gamma distribution.  Not the gamma function!
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      
     |      The probability distribution function is:
     |      
     |                  x ** (alpha - 1) * math.exp(-x / beta)
     |        pdf(x) =  --------------------------------------
     |                    math.gamma(alpha) * beta ** alpha
     |  
     |  gauss(self, mu, sigma)
     |      Gaussian distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.  This is
     |      slightly faster than the normalvariate() function.
     |      
     |      Not thread-safe without a lock around calls.
     |  
     |  getstate(self)
     |      Return internal state; can be passed to setstate() later.
     |  
     |  lognormvariate(self, mu, sigma)
     |      Log normal distribution.
     |      
     |      If you take the natural logarithm of this distribution, you'll get a
     |      normal distribution with mean mu and standard deviation sigma.
     |      mu can have any value, and sigma must be greater than zero.
     |  
     |  normalvariate(self, mu, sigma)
     |      Normal distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.
     |  
     |  paretovariate(self, alpha)
     |      Pareto distribution.  alpha is the shape parameter.
     |  
     |  randint(self, a, b)
     |      Return random integer in range [a, b], including both end points.
     |  
     |  randrange(self, start, stop=None, step=1, _int=<class 'int'>)
     |      Choose a random item from range(start, stop[, step]).
     |      
     |      This fixes the problem with randint() which includes the
     |      endpoint; in Python this is usually not what you want.
     |  
     |  sample(self, population, k)
     |      Chooses k unique random elements from a population sequence or set.
     |      
     |      Returns a new list containing elements from the population while
     |      leaving the original population unchanged.  The resulting list is
     |      in selection order so that all sub-slices will also be valid random
     |      samples.  This allows raffle winners (the sample) to be partitioned
     |      into grand prize and second place winners (the subslices).
     |      
     |      Members of the population need not be hashable or unique.  If the
     |      population contains repeats, then each occurrence is a possible
     |      selection in the sample.
     |      
     |      To choose a sample in a range of integers, use range as an argument.
     |      This is especially fast and space efficient for sampling from a
     |      large population:   sample(range(10000000), 60)
     |  
     |  seed(self, a=None, version=2)
     |      Initialize internal state from hashable object.
     |      
     |      None or no argument seeds from current time or from an operating
     |      system specific randomness source if available.
     |      
     |      If *a* is an int, all bits are used.
     |      
     |      For version 2 (the default), all of the bits are used if *a* is a str,
     |      bytes, or bytearray.  For version 1 (provided for reproducing random
     |      sequences from older versions of Python), the algorithm for str and
     |      bytes generates a narrower range of seeds.
     |  
     |  setstate(self, state)
     |      Restore internal state from object returned by getstate().
     |  
     |  shuffle(self, x, random=None)
     |      Shuffle list x in place, and return None.
     |      
     |      Optional argument random is a 0-argument function returning a
     |      random float in [0.0, 1.0); if it is the default None, the
     |      standard random.random will be used.
     |  
     |  triangular(self, low=0.0, high=1.0, mode=None)
     |      Triangular distribution.
     |      
     |      Continuous distribution bounded by given lower and upper limits,
     |      and having a given mode value in-between.
     |      
     |      http://en.wikipedia.org/wiki/Triangular_distribution
     |  
     |  uniform(self, a, b)
     |      Get a random number in the range [a, b) or [a, b] depending on rounding.
     |  
     |  vonmisesvariate(self, mu, kappa)
     |      Circular data distribution.
     |      
     |      mu is the mean angle, expressed in radians between 0 and 2*pi, and
     |      kappa is the concentration parameter, which must be greater than or
     |      equal to zero.  If kappa is equal to zero, this distribution reduces
     |      to a uniform random angle over the range 0 to 2*pi.
     |  
     |  weibullvariate(self, alpha, beta)
     |      Weibull distribution.
     |      
     |      alpha is the scale parameter and beta is the shape parameter.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  VERSION = 3
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _random.Random:
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  getrandbits(...)
     |      getrandbits(k) -> x.  Generates an int with k random bits.
     |  
     |  random(...)
     |      random() -> x in the interval [0, 1).
    
    class SystemRandom(Random)
     |  Alternate random number generator using sources provided
     |  by the operating system (such as /dev/urandom on Unix or
     |  CryptGenRandom on Windows).
     |  
     |   Not available on all systems (see os.urandom() for details).
     |  
     |  Method resolution order:
     |      SystemRandom
     |      Random
     |      _random.Random
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  getrandbits(self, k)
     |      getrandbits(k) -> x.  Generates an int with k random bits.
     |  
     |  getstate = _notimplemented(self, *args, **kwds)
     |  
     |  random(self)
     |      Get the next random number in the range [0.0, 1.0).
     |  
     |  seed(self, *args, **kwds)
     |      Stub method.  Not used for a system random number generator.
     |  
     |  setstate = _notimplemented(self, *args, **kwds)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Random:
     |  
     |  __getstate__(self)
     |      # Issue 17489: Since __reduce__ was defined to fix #759889 this is no
     |      # longer called; we leave it here because it has been here since random was
     |      # rewritten back in 2001 and why risk breaking something.
     |  
     |  __init__(self, x=None)
     |      Initialize an instance.
     |      
     |      Optional argument x controls seeding, as for Random.seed().
     |  
     |  __reduce__(self)
     |      helper for pickle
     |  
     |  __setstate__(self, state)
     |  
     |  betavariate(self, alpha, beta)
     |      Beta distribution.
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      Returned values range between 0 and 1.
     |  
     |  choice(self, seq)
     |      Choose a random element from a non-empty sequence.
     |  
     |  choices(self, population, weights=None, *, cum_weights=None, k=1)
     |      Return a k sized list of population elements chosen with replacement.
     |      
     |      If the relative weights or cumulative weights are not specified,
     |      the selections are made with equal probability.
     |  
     |  expovariate(self, lambd)
     |      Exponential distribution.
     |      
     |      lambd is 1.0 divided by the desired mean.  It should be
     |      nonzero.  (The parameter would be called "lambda", but that is
     |      a reserved word in Python.)  Returned values range from 0 to
     |      positive infinity if lambd is positive, and from negative
     |      infinity to 0 if lambd is negative.
     |  
     |  gammavariate(self, alpha, beta)
     |      Gamma distribution.  Not the gamma function!
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      
     |      The probability distribution function is:
     |      
     |                  x ** (alpha - 1) * math.exp(-x / beta)
     |        pdf(x) =  --------------------------------------
     |                    math.gamma(alpha) * beta ** alpha
     |  
     |  gauss(self, mu, sigma)
     |      Gaussian distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.  This is
     |      slightly faster than the normalvariate() function.
     |      
     |      Not thread-safe without a lock around calls.
     |  
     |  lognormvariate(self, mu, sigma)
     |      Log normal distribution.
     |      
     |      If you take the natural logarithm of this distribution, you'll get a
     |      normal distribution with mean mu and standard deviation sigma.
     |      mu can have any value, and sigma must be greater than zero.
     |  
     |  normalvariate(self, mu, sigma)
     |      Normal distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.
     |  
     |  paretovariate(self, alpha)
     |      Pareto distribution.  alpha is the shape parameter.
     |  
     |  randint(self, a, b)
     |      Return random integer in range [a, b], including both end points.
     |  
     |  randrange(self, start, stop=None, step=1, _int=<class 'int'>)
     |      Choose a random item from range(start, stop[, step]).
     |      
     |      This fixes the problem with randint() which includes the
     |      endpoint; in Python this is usually not what you want.
     |  
     |  sample(self, population, k)
     |      Chooses k unique random elements from a population sequence or set.
     |      
     |      Returns a new list containing elements from the population while
     |      leaving the original population unchanged.  The resulting list is
     |      in selection order so that all sub-slices will also be valid random
     |      samples.  This allows raffle winners (the sample) to be partitioned
     |      into grand prize and second place winners (the subslices).
     |      
     |      Members of the population need not be hashable or unique.  If the
     |      population contains repeats, then each occurrence is a possible
     |      selection in the sample.
     |      
     |      To choose a sample in a range of integers, use range as an argument.
     |      This is especially fast and space efficient for sampling from a
     |      large population:   sample(range(10000000), 60)
     |  
     |  shuffle(self, x, random=None)
     |      Shuffle list x in place, and return None.
     |      
     |      Optional argument random is a 0-argument function returning a
     |      random float in [0.0, 1.0); if it is the default None, the
     |      standard random.random will be used.
     |  
     |  triangular(self, low=0.0, high=1.0, mode=None)
     |      Triangular distribution.
     |      
     |      Continuous distribution bounded by given lower and upper limits,
     |      and having a given mode value in-between.
     |      
     |      http://en.wikipedia.org/wiki/Triangular_distribution
     |  
     |  uniform(self, a, b)
     |      Get a random number in the range [a, b) or [a, b] depending on rounding.
     |  
     |  vonmisesvariate(self, mu, kappa)
     |      Circular data distribution.
     |      
     |      mu is the mean angle, expressed in radians between 0 and 2*pi, and
     |      kappa is the concentration parameter, which must be greater than or
     |      equal to zero.  If kappa is equal to zero, this distribution reduces
     |      to a uniform random angle over the range 0 to 2*pi.
     |  
     |  weibullvariate(self, alpha, beta)
     |      Weibull distribution.
     |      
     |      alpha is the scale parameter and beta is the shape parameter.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Random:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from Random:
     |  
     |  VERSION = 3
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _random.Random:
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.

FUNCTIONS
    betavariate(alpha, beta) method of Random instance
        Beta distribution.
        
        Conditions on the parameters are alpha > 0 and beta > 0.
        Returned values range between 0 and 1.
    
    choice(seq) method of Random instance
        Choose a random element from a non-empty sequence.
    
    choices(population, weights=None, *, cum_weights=None, k=1) method of Random instance
        Return a k sized list of population elements chosen with replacement.
        
        If the relative weights or cumulative weights are not specified,
        the selections are made with equal probability.
    
    expovariate(lambd) method of Random instance
        Exponential distribution.
        
        lambd is 1.0 divided by the desired mean.  It should be
        nonzero.  (The parameter would be called "lambda", but that is
        a reserved word in Python.)  Returned values range from 0 to
        positive infinity if lambd is positive, and from negative
        infinity to 0 if lambd is negative.
    
    gammavariate(alpha, beta) method of Random instance
        Gamma distribution.  Not the gamma function!
        
        Conditions on the parameters are alpha > 0 and beta > 0.
        
        The probability distribution function is:
        
                    x ** (alpha - 1) * math.exp(-x / beta)
          pdf(x) =  --------------------------------------
                      math.gamma(alpha) * beta ** alpha
    
    gauss(mu, sigma) method of Random instance
        Gaussian distribution.
        
        mu is the mean, and sigma is the standard deviation.  This is
        slightly faster than the normalvariate() function.
        
        Not thread-safe without a lock around calls.
    
    getrandbits(...) method of Random instance
        getrandbits(k) -> x.  Generates an int with k random bits.
    
    getstate() method of Random instance
        Return internal state; can be passed to setstate() later.
    
    lognormvariate(mu, sigma) method of Random instance
        Log normal distribution.
        
        If you take the natural logarithm of this distribution, you'll get a
        normal distribution with mean mu and standard deviation sigma.
        mu can have any value, and sigma must be greater than zero.
    
    normalvariate(mu, sigma) method of Random instance
        Normal distribution.
        
        mu is the mean, and sigma is the standard deviation.
    
    paretovariate(alpha) method of Random instance
        Pareto distribution.  alpha is the shape parameter.
    
    randint(a, b) method of Random instance
        Return random integer in range [a, b], including both end points.
    
    random(...) method of Random instance
        random() -> x in the interval [0, 1).
    
    randrange(start, stop=None, step=1, _int=<class 'int'>) method of Random instance
        Choose a random item from range(start, stop[, step]).
        
        This fixes the problem with randint() which includes the
        endpoint; in Python this is usually not what you want.
    
    sample(population, k) method of Random instance
        Chooses k unique random elements from a population sequence or set.
        
        Returns a new list containing elements from the population while
        leaving the original population unchanged.  The resulting list is
        in selection order so that all sub-slices will also be valid random
        samples.  This allows raffle winners (the sample) to be partitioned
        into grand prize and second place winners (the subslices).
        
        Members of the population need not be hashable or unique.  If the
        population contains repeats, then each occurrence is a possible
        selection in the sample.
        
        To choose a sample in a range of integers, use range as an argument.
        This is especially fast and space efficient for sampling from a
        large population:   sample(range(10000000), 60)
    
    seed(a=None, version=2) method of Random instance
        Initialize internal state from hashable object.
        
        None or no argument seeds from current time or from an operating
        system specific randomness source if available.
        
        If *a* is an int, all bits are used.
        
        For version 2 (the default), all of the bits are used if *a* is a str,
        bytes, or bytearray.  For version 1 (provided for reproducing random
        sequences from older versions of Python), the algorithm for str and
        bytes generates a narrower range of seeds.
    
    setstate(state) method of Random instance
        Restore internal state from object returned by getstate().
    
    shuffle(x, random=None) method of Random instance
        Shuffle list x in place, and return None.
        
        Optional argument random is a 0-argument function returning a
        random float in [0.0, 1.0); if it is the default None, the
        standard random.random will be used.
    
    triangular(low=0.0, high=1.0, mode=None) method of Random instance
        Triangular distribution.
        
        Continuous distribution bounded by given lower and upper limits,
        and having a given mode value in-between.
        
        http://en.wikipedia.org/wiki/Triangular_distribution
    
    uniform(a, b) method of Random instance
        Get a random number in the range [a, b) or [a, b] depending on rounding.
    
    vonmisesvariate(mu, kappa) method of Random instance
        Circular data distribution.
        
        mu is the mean angle, expressed in radians between 0 and 2*pi, and
        kappa is the concentration parameter, which must be greater than or
        equal to zero.  If kappa is equal to zero, this distribution reduces
        to a uniform random angle over the range 0 to 2*pi.
    
    weibullvariate(alpha, beta) method of Random instance
        Weibull distribution.
        
        alpha is the scale parameter and beta is the shape parameter.

DATA
    __all__ = ['Random', 'seed', 'random', 'uniform', 'randint', 'choice',...

FILE
    c:\python\python36-32\lib\random.py


>>> import matplotlib
	       
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    import matplotlib
ModuleNotFoundError: No module named 'matplotlib'
>>> 
== RESTART: C:/Python/Python36-32/file_handling_with_Exception_Handling.py ==
Error: can't find file or read 
[Errno 2] No such file or directory: 'C:\\Python\\Python36-32\\file handling\\sample_001.txt'
Traceback (most recent call last):
  File "C:/Python/Python36-32/file_handling_with_Exception_Handling.py", line 13, in <module>
    fh.close()
NameError: name 'fh' is not defined
>>> 
== RESTART: C:/Python/Python36-32/file_handling_with_Exception_Handling.py ==
Error: can't find file or read 
[Errno 2] No such file or directory: 'C:\\Python\\Python36-32\\file handling\\sample_001.txt'
Traceback (most recent call last):
  File "C:/Python/Python36-32/file_handling_with_Exception_Handling.py", line 13, in <module>
    fh.close()
NameError: name 'fh' is not defined
>>> 
== RESTART: C:/Python/Python36-32/file_handling_with_Exception_Handling.py ==
division by zero
>>> 
== RESTART: C:/Python/Python36-32/file_handling_with_Exception_Handling.py ==
Error: can't find file or read 
not writable
>>> import matplotlib
	       
>>> help(matplotlib)
	       
Help on package matplotlib:

NAME
    matplotlib - This is an object-oriented plotting library.

DESCRIPTION
    A procedural interface is provided by the companion pyplot module,
    which may be imported directly, e.g.::
    
        import matplotlib.pyplot as plt
    
    or using ipython::
    
        ipython
    
    at your terminal, followed by::
    
        In [1]: %matplotlib
        In [2]: import matplotlib.pyplot as plt
    
    at the ipython shell prompt.
    
    For the most part, direct use of the object-oriented library is
    encouraged when programming; pyplot is primarily for working
    interactively.  The
    exceptions are the pyplot commands :func:`~matplotlib.pyplot.figure`,
    :func:`~matplotlib.pyplot.subplot`,
    :func:`~matplotlib.pyplot.subplots`, and
    :func:`~pyplot.savefig`, which can greatly simplify scripting.
    
    Modules include:
    
        :mod:`matplotlib.axes`
            defines the :class:`~matplotlib.axes.Axes` class.  Most pylab
            commands are wrappers for :class:`~matplotlib.axes.Axes`
            methods.  The axes module is the highest level of OO access to
            the library.
    
        :mod:`matplotlib.figure`
            defines the :class:`~matplotlib.figure.Figure` class.
    
        :mod:`matplotlib.artist`
            defines the :class:`~matplotlib.artist.Artist` base class for
            all classes that draw things.
    
        :mod:`matplotlib.lines`
            defines the :class:`~matplotlib.lines.Line2D` class for
            drawing lines and markers
    
        :mod:`matplotlib.patches`
            defines classes for drawing polygons
    
        :mod:`matplotlib.text`
            defines the :class:`~matplotlib.text.Text`,
            :class:`~matplotlib.text.TextWithDash`, and
            :class:`~matplotlib.text.Annotate` classes
    
        :mod:`matplotlib.image`
            defines the :class:`~matplotlib.image.AxesImage` and
            :class:`~matplotlib.image.FigureImage` classes
    
        :mod:`matplotlib.collections`
            classes for efficient drawing of groups of lines or polygons
    
        :mod:`matplotlib.colors`
            classes for interpreting color specifications and for making
            colormaps
    
        :mod:`matplotlib.cm`
            colormaps and the :class:`~matplotlib.image.ScalarMappable`
            mixin class for providing color mapping functionality to other
            classes
    
        :mod:`matplotlib.ticker`
            classes for calculating tick mark locations and for formatting
            tick labels
    
        :mod:`matplotlib.backends`
            a subpackage with modules for various gui libraries and output
            formats
    
    The base matplotlib namespace includes:
    
        :data:`~matplotlib.rcParams`
            a global dictionary of default configuration settings.  It is
            initialized by code which may be overridden by a matplotlibrc
            file.
    
        :func:`~matplotlib.rc`
            a function for setting groups of rcParams values
    
        :func:`~matplotlib.use`
            a function for setting the matplotlib backend.  If used, this
            function must be called immediately after importing matplotlib
            for the first time.  In particular, it must be called
            **before** importing pylab (if pylab is imported).
    
    matplotlib was initially written by John D. Hunter (1968-2012) and is now
    developed and maintained by a host of others.
    
    Occasionally the internal documentation (python docstrings) will refer
    to MATLAB&reg;, a registered trademark of The MathWorks, Inc.

PACKAGE CONTENTS
    _animation_data
    _cm
    _cm_listed
    _color_data
    _constrained_layout
    _contour
    _image
    _layoutbox
    _mathtext_data
    _path
    _png
    _pylab_helpers
    _qhull
    _tri
    _version
    _windowing
    afm
    animation
    artist
    axes (package)
    axis
    backend_bases
    backend_managers
    backend_tools
    backends (package)
    bezier
    blocking_input
    category
    cbook (package)
    cm
    collections
    colorbar
    colors
    compat (package)
    container
    contour
    dates
    docstring
    dviread
    figure
    font_manager
    fontconfig_pattern
    ft2font
    gridspec
    hatch
    image
    legend
    legend_handler
    lines
    markers
    mathtext
    mlab
    offsetbox
    patches
    path
    patheffects
    projections (package)
    pylab
    pyplot
    quiver
    rcsetup
    sankey
    scale
    sphinxext (package)
    spines
    stackplot
    streamplot
    style (package)
    table
    testing (package)
    texmanager
    text
    textpath
    ticker
    tight_bbox
    tight_layout
    transforms
    tri (package)
    ttconv
    type1font
    units
    widgets

SUBMODULES
    _backports
    subprocess

CLASSES
    builtins.dict(builtins.object)
        RcParams(collections.abc.MutableMapping, builtins.dict)
    builtins.object
        Verbose
    collections.abc.MutableMapping(collections.abc.Mapping)
        RcParams(collections.abc.MutableMapping, builtins.dict)
    
    class RcParams(collections.abc.MutableMapping, builtins.dict)
     |  A dictionary object including validation
     |  
     |  validating functions are defined and associated with rc parameters in
     |  :mod:`matplotlib.rcsetup`
     |  
     |  Method resolution order:
     |      RcParams
     |      collections.abc.MutableMapping
     |      collections.abc.Mapping
     |      collections.abc.Collection
     |      collections.abc.Sized
     |      collections.abc.Iterable
     |      collections.abc.Container
     |      builtins.dict
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __getitem__(self, key)
     |      x.__getitem__(y) <==> x[y]
     |  
     |  __init__(self, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __iter__(self)
     |      Yield sorted list of keys.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  __setitem__(self, key, val)
     |      Set self[key] to value.
     |  
     |  __str__(self)
     |      Return str(self).
     |  
     |  find_all(self, pattern)
     |      Return the subset of this RcParams dictionary whose keys match,
     |      using :func:`re.search`, the given ``pattern``.
     |      
     |      .. note::
     |      
     |          Changes to the returned dictionary are *not* propagated to
     |          the parent RcParams dictionary.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __abstractmethods__ = frozenset({'__delitem__', '__len__'})
     |  
     |  msg_backend_obsolete = 'The {} rcParam was deprecated in version 2.2. ...
     |  
     |  msg_depr = '%s is deprecated and replaced with %s; please use the latt...
     |  
     |  msg_depr_ignore = '%s is deprecated and ignored. Use %s instead.'
     |  
     |  msg_depr_set = '%s is deprecated. Please remove it from your matplotli...
     |  
     |  msg_obsolete = '%s is obsolete. Please remove it from your matplotlibr...
     |  
     |  validate = {'_internal.classic_mode': <function validate_bool>, 'agg.p...
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.MutableMapping:
     |  
     |  __delitem__(self, key)
     |  
     |  clear(self)
     |      D.clear() -> None.  Remove all items from D.
     |  
     |  pop(self, key, default=<object object at 0x032790B0>)
     |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
     |      If key is not found, d is returned if given, otherwise KeyError is raised.
     |  
     |  popitem(self)
     |      D.popitem() -> (k, v), remove and return some (key, value) pair
     |      as a 2-tuple; but raise KeyError if D is empty.
     |  
     |  setdefault(self, key, default=None)
     |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
     |  
     |  update(*args, **kwds)
     |      D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
     |      If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
     |      If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
     |      In either case, this is followed by: for k, v in F.items(): D[k] = v
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.Mapping:
     |  
     |  __contains__(self, key)
     |  
     |  __eq__(self, other)
     |      Return self==value.
     |  
     |  get(self, key, default=None)
     |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
     |  
     |  items(self)
     |      D.items() -> a set-like object providing a view on D's items
     |  
     |  keys(self)
     |      D.keys() -> a set-like object providing a view on D's keys
     |  
     |  values(self)
     |      D.values() -> an object providing a view on D's values
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from collections.abc.Mapping:
     |  
     |  __hash__ = None
     |  
     |  __reversed__ = None
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from collections.abc.Collection:
     |  
     |  __subclasshook__(C) from abc.ABCMeta
     |      Abstract classes can override this to customize issubclass().
     |      
     |      This is invoked early on by abc.ABCMeta.__subclasscheck__().
     |      It should return True, False or NotImplemented.  If it returns
     |      NotImplemented, the normal algorithm is used.  Otherwise, it
     |      overrides the normal algorithm (and the outcome is cached).
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.Sized:
     |  
     |  __len__(self)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.dict:
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __sizeof__(...)
     |      D.__sizeof__() -> size of D in memory, in bytes
     |  
     |  copy(...)
     |      D.copy() -> a shallow copy of D
     |  
     |  fromkeys(iterable, value=None, /) from abc.ABCMeta
     |      Returns a new dict with keys from iterable and values equal to value.
    
    class Verbose(builtins.object)
     |  A class to handle reporting.  Set the fileo attribute to any file
     |  instance to handle the output.  Default is sys.stdout
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |      .. deprecated:: 2.2
     |          matplotlib.verbose is deprecated;
     |      Command line argument --verbose-LEVEL is deprecated.
     |      This functionality is now provided by the standard
     |      python logging library.  To get more (or less) logging output:
     |          import logging
     |          logger = logging.getLogger('matplotlib')
     |          logger.set_level(logging.INFO)
     |      
     |      \
     |  
     |  ge(self, level)
     |      .. deprecated:: 2.2
     |          matplotlib.verbose is deprecated;
     |      Command line argument --verbose-LEVEL is deprecated.
     |      This functionality is now provided by the standard
     |      python logging library.  To get more (or less) logging output:
     |          import logging
     |          logger = logging.getLogger('matplotlib')
     |          logger.set_level(logging.INFO)
     |      
     |      return true if self.level is >= level
     |  
     |  report(self, s, level='helpful')
     |      .. deprecated:: 2.2
     |          matplotlib.verbose is deprecated;
     |      Command line argument --verbose-LEVEL is deprecated.
     |      This functionality is now provided by the standard
     |      python logging library.  To get more (or less) logging output:
     |          import logging
     |          logger = logging.getLogger('matplotlib')
     |          logger.set_level(logging.INFO)
     |      
     |      print message s to self.fileo if self.level>=level.  Return
     |      value indicates whether a message was issued
     |  
     |  set_fileo(self, fname)
     |      .. deprecated:: 2.2
     |          matplotlib.verbose is deprecated;
     |      Command line argument --verbose-LEVEL is deprecated.
     |      This functionality is now provided by the standard
     |      python logging library.  To get more (or less) logging output:
     |          import logging
     |          logger = logging.getLogger('matplotlib')
     |          logger.set_level(logging.INFO)
     |      
     |      \
     |  
     |  set_level(self, level)
     |      .. deprecated:: 2.2
     |          matplotlib.verbose is deprecated;
     |      Command line argument --verbose-LEVEL is deprecated.
     |      This functionality is now provided by the standard
     |      python logging library.  To get more (or less) logging output:
     |          import logging
     |          logger = logging.getLogger('matplotlib')
     |          logger.set_level(logging.INFO)
     |      
     |      set the verbosity to one of the Verbose.levels strings
     |  
     |  wrap(self, fmt, func, level='helpful', always=True)
     |      .. deprecated:: 2.2
     |          matplotlib.verbose is deprecated;
     |      Command line argument --verbose-LEVEL is deprecated.
     |      This functionality is now provided by the standard
     |      python logging library.  To get more (or less) logging output:
     |          import logging
     |          logger = logging.getLogger('matplotlib')
     |          logger.set_level(logging.INFO)
     |      
     |      return a callable function that wraps func and reports it
     |      output through the verbose handler if current verbosity level
     |      is higher than level
     |      
     |      if always is True, the report will occur on every function
     |      call; otherwise only on the first time the function is called
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  levels = ('silent', 'helpful', 'debug', 'debug-annoying')
     |  
     |  vald = {'debug': 2, 'debug-annoying': 3, 'helpful': 1, 'silent': 0}

FUNCTIONS
    checkdep_dvipng()
    
    checkdep_ghostscript()
    
    checkdep_inkscape()
    
    checkdep_pdftops()
    
    checkdep_ps_distiller(s)
    
    checkdep_tex()
        .. deprecated:: 2.1
            The checkdep_tex function was deprecated in version 2.1.
        
        \
    
    checkdep_usetex(s)
    
    checkdep_xmllint()
        .. deprecated:: 2.1
            The checkdep_xmllint function was deprecated in version 2.1.
        
        \
    
    compare_versions(a, b)
        return True if a is greater than or equal to b
    
    get_backend()
        Return the name of the current backend.
    
    get_cachedir = wrapper(*args, **kwargs)
        Return the location of the cache directory.
        
        The procedure used to find the directory is the same as for
        _get_config_dir, except using `$XDG_CACHE_HOME`/`~/.cache` instead.
    
    get_configdir = wrapper(*args, **kwargs)
        Return the string representing the configuration directory.
        
        The directory is chosen as follows:
        
        1. If the MPLCONFIGDIR environment variable is supplied, choose that.
        
        2a. On Linux, follow the XDG specification and look first in
            `$XDG_CONFIG_HOME`, if defined, or `$HOME/.config`.
        
        2b. On other platforms, choose `$HOME/.matplotlib`.
        
        3. If the chosen directory exists and is writable, use that as the
           configuration directory.
        4. If possible, create a temporary directory, and use it as the
           configuration directory.
        5. A writable directory could not be found or created; return None.
    
    get_data_path = wrapper(*args, **kwargs)
    
    get_home = wrapper(*args, **kwargs)
        Find user's home directory if possible.
        Otherwise, returns None.
        
        :see:
            http://mail.python.org/pipermail/python-list/2005-February/325395.html
    
    get_py2exe_datafiles()
    
    interactive(b)
        Set interactive mode to boolean b.
        
        If b is True, then draw after every plotting command, e.g., after xlabel
    
    is_interactive()
        Return true if plot mode is interactive
    
    is_url(filename)
        Return True if string is an http, ftp, or file URL path.
    
    matplotlib_fname()
        Get the location of the config file.
        
        The file location is determined in the following order
        
        - `$PWD/matplotlibrc`
        
        - `$MATPLOTLIBRC` if it is a file (or a named pipe, which can be created
          e.g. by process substitution)
        
        - `$MATPLOTLIBRC/matplotlibrc`
        
        - `$MPLCONFIGDIR/matplotlibrc`
        
        - On Linux,
        
              - `$XDG_CONFIG_HOME/matplotlib/matplotlibrc` (if
                $XDG_CONFIG_HOME is defined)
        
              - or `$HOME/.config/matplotlib/matplotlibrc` (if
                $XDG_CONFIG_HOME is not defined)
        
        - On other platforms,
        
             - `$HOME/.matplotlib/matplotlibrc` if `$HOME` is defined.
        
        - Lastly, it looks in `$MATPLOTLIBDATA/matplotlibrc` for a
          system-defined copy.
    
    rc(group, **kwargs)
        Set the current rc params.  Group is the grouping for the rc, e.g.,
        for ``lines.linewidth`` the group is ``lines``, for
        ``axes.facecolor``, the group is ``axes``, and so on.  Group may
        also be a list or tuple of group names, e.g., (*xtick*, *ytick*).
        *kwargs* is a dictionary attribute name/value pairs, e.g.,::
        
          rc('lines', linewidth=2, color='r')
        
        sets the current rc params and is equivalent to::
        
          rcParams['lines.linewidth'] = 2
          rcParams['lines.color'] = 'r'
        
        The following aliases are available to save typing for interactive
        users:
        
        =====   =================
        Alias   Property
        =====   =================
        'lw'    'linewidth'
        'ls'    'linestyle'
        'c'     'color'
        'fc'    'facecolor'
        'ec'    'edgecolor'
        'mew'   'markeredgewidth'
        'aa'    'antialiased'
        =====   =================
        
        Thus you could abbreviate the above rc command as::
        
              rc('lines', lw=2, c='r')
        
        
        Note you can use python's kwargs dictionary facility to store
        dictionaries of default parameters.  e.g., you can customize the
        font rc as follows::
        
          font = {'family' : 'monospace',
                  'weight' : 'bold',
                  'size'   : 'larger'}
        
          rc('font', **font)  # pass in the font dict as kwargs
        
        This enables you to easily switch between several configurations.  Use
        ``matplotlib.style.use('default')`` or :func:`~matplotlib.rcdefaults` to
        restore the default rc params after changes.
    
    rc_context(rc=None, fname=None)
        Return a context manager for managing rc settings.
        
        This allows one to do::
        
            with mpl.rc_context(fname='screen.rc'):
                plt.plot(x, a)
                with mpl.rc_context(fname='print.rc'):
                    plt.plot(x, b)
                plt.plot(x, c)
        
        The 'a' vs 'x' and 'c' vs 'x' plots would have settings from
        'screen.rc', while the 'b' vs 'x' plot would have settings from
        'print.rc'.
        
        A dictionary can also be passed to the context manager::
        
            with mpl.rc_context(rc={'text.usetex': True}, fname='screen.rc'):
                plt.plot(x, a)
        
        The 'rc' dictionary takes precedence over the settings loaded from
        'fname'.  Passing a dictionary only is also valid. For example a
        common usage is::
        
            with mpl.rc_context(rc={'interactive': False}):
                fig, ax = plt.subplots()
                ax.plot(range(3), range(3))
                fig.savefig('A.png', format='png')
                plt.close(fig)
    
    rc_file(fname)
        Update rc params from file.
    
    rc_file_defaults()
        Restore the rc params from the original rc file loaded by Matplotlib.
    
    rc_params(fail_on_error=False)
        Return a :class:`matplotlib.RcParams` instance from the
        default matplotlib rc file.
    
    rc_params_from_file(fname, fail_on_error=False, use_default_template=True)
        Return :class:`matplotlib.RcParams` from the contents of the given file.
        
        Parameters
        ----------
        fname : str
            Name of file parsed for matplotlib settings.
        fail_on_error : bool
            If True, raise an error when the parser fails to convert a parameter.
        use_default_template : bool
            If True, initialize with default parameters before updating with those
            in the given file. If False, the configuration class only contains the
            parameters specified in the file. (Useful for updating dicts.)
    
    rcdefaults()
        Restore the rc params from Matplotlib's internal defaults.
        
        See Also
        --------
        rc_file_defaults :
            Restore the rc params from the rc file originally loaded by Matplotlib.
        matplotlib.style.use :
            Use a specific style file.  Call ``style.use('default')`` to restore
            the default style.
    
    test(verbosity=None, coverage=False, switch_backend_warn=True, recursionlimit=0, **kwargs)
        run the matplotlib test suite
    
    tk_window_focus()
        Return true if focus maintenance under TkAgg on win32 is on.
        This currently works only for python.exe and IPython.exe.
        Both IDLE and Pythonwin.exe fail badly when tk_window_focus is on.
    
    use(arg, warn=True, force=False)
        Set the matplotlib backend to one of the known backends.
        
        The argument is case-insensitive. *warn* specifies whether a
        warning should be issued if a backend has already been set up.
        *force* is an **experimental** flag that tells matplotlib to
        attempt to initialize a new backend by reloading the backend
        module.
        
        .. note::
        
            This function must be called *before* importing pyplot for
            the first time; or, if you are not using pyplot, it must be called
            before importing matplotlib.backends.  If warn is True, a warning
            is issued if you try and call this after pylab or pyplot have been
            loaded.  In certain black magic use cases, e.g.
            :func:`pyplot.switch_backend`, we are doing the reloading necessary to
            make the backend switch work (in some cases, e.g., pure image
            backends) so one can set warn=False to suppress the warnings.
        
        To find out which backend is currently set, see
        :func:`matplotlib.get_backend`.

DATA
    URL_REGEX = re.compile('http://|https://|ftp://|file://|file:\\\\')
    __bibtex__ = '@Article{Hunter:2007,\n  Author    = {Hunter, J. ...ishe...
    __version__numpy__ = '1.7.1'
    __warningregistry__ = {'version': 9, ("matplotlib.verbose is deprecate...
    absolute_import = _Feature((2, 5, 0, 'alpha', 1), (3, 0, 0, 'alpha', 0...
    defaultParams = {'_internal.classic_mode': [False, <function validate_...
    default_test_modules = ['matplotlib.tests', 'matplotlib.sphinxext.test...
    division = _Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192...
    print_function = _Feature((2, 6, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0)...
    rcParams = RcParams({'_internal.classic_mode': False,
         ...nor.widt...
    rcParamsDefault = RcParams({'_internal.classic_mode': False,
         ...n...
    rcParamsOrig = {'_internal.classic_mode': False, 'agg.path.chunksize':...
    verbose = <matplotlib.Verbose object>

VERSION
    2.2.2

FILE
    c:\python\python36-32\lib\site-packages\matplotlib\__init__.py


>>> import table
		    
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    import table
ModuleNotFoundError: No module named 'table'
>>> import tables
		    
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    import tables
ModuleNotFoundError: No module named 'tables'
>>> import builtins
		    
>>> help(builtins)
		    
Help on built-in module builtins:

NAME
    builtins - Built-in functions, exceptions, and other objects.

DESCRIPTION
    Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.

CLASSES
    object
        BaseException
            Exception
                ArithmeticError
                    FloatingPointError
                    OverflowError
                    ZeroDivisionError
                AssertionError
                AttributeError
                BufferError
                EOFError
                ImportError
                    ModuleNotFoundError
                LookupError
                    IndexError
                    KeyError
                MemoryError
                NameError
                    UnboundLocalError
                OSError
                    BlockingIOError
                    ChildProcessError
                    ConnectionError
                        BrokenPipeError
                        ConnectionAbortedError
                        ConnectionRefusedError
                        ConnectionResetError
                    FileExistsError
                    FileNotFoundError
                    InterruptedError
                    IsADirectoryError
                    NotADirectoryError
                    PermissionError
                    ProcessLookupError
                    TimeoutError
                ReferenceError
                RuntimeError
                    NotImplementedError
                    RecursionError
                StopAsyncIteration
                StopIteration
                SyntaxError
                    IndentationError
                        TabError
                SystemError
                TypeError
                ValueError
                    UnicodeError
                        UnicodeDecodeError
                        UnicodeEncodeError
                        UnicodeTranslateError
                Warning
                    BytesWarning
                    DeprecationWarning
                    FutureWarning
                    ImportWarning
                    PendingDeprecationWarning
                    ResourceWarning
                    RuntimeWarning
                    SyntaxWarning
                    UnicodeWarning
                    UserWarning
            GeneratorExit
            KeyboardInterrupt
            SystemExit
        bytearray
        bytes
        classmethod
        complex
        dict
        enumerate
        filter
        float
        frozenset
        int
            bool
        list
        map
        memoryview
        property
        range
        reversed
        set
        slice
        staticmethod
        str
        super
        tuple
        type
        zip
    
    class ArithmeticError(Exception)
     |  Base class for arithmetic errors.
     |  
     |  Method resolution order:
     |      ArithmeticError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class AssertionError(Exception)
     |  Assertion failed.
     |  
     |  Method resolution order:
     |      AssertionError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class AttributeError(Exception)
     |  Attribute not found.
     |  
     |  Method resolution order:
     |      AttributeError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class BaseException(object)
     |  Common base class for all exceptions
     |  
     |  Methods defined here:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class BlockingIOError(OSError)
     |  I/O operation would block.
     |  
     |  Method resolution order:
     |      BlockingIOError
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from OSError:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from OSError:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class BrokenPipeError(ConnectionError)
     |  Broken pipe.
     |  
     |  Method resolution order:
     |      BrokenPipeError
     |      ConnectionError
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from OSError:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from OSError:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class BufferError(Exception)
     |  Buffer error.
     |  
     |  Method resolution order:
     |      BufferError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class BytesWarning(Warning)
     |  Base class for warnings about bytes and buffer related problems, mostly
     |  related to conversion from str or comparing to str.
     |  
     |  Method resolution order:
     |      BytesWarning
     |      Warning
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class ChildProcessError(OSError)
     |  Child process error.
     |  
     |  Method resolution order:
     |      ChildProcessError
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from OSError:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from OSError:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class ConnectionAbortedError(ConnectionError)
     |  Connection aborted.
     |  
     |  Method resolution order:
     |      ConnectionAbortedError
     |      ConnectionError
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from OSError:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from OSError:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class ConnectionError(OSError)
     |  Connection error.
     |  
     |  Method resolution order:
     |      ConnectionError
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from OSError:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from OSError:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class ConnectionRefusedError(ConnectionError)
     |  Connection refused.
     |  
     |  Method resolution order:
     |      ConnectionRefusedError
     |      ConnectionError
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from OSError:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from OSError:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class ConnectionResetError(ConnectionError)
     |  Connection reset.
     |  
     |  Method resolution order:
     |      ConnectionResetError
     |      ConnectionError
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from OSError:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from OSError:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class DeprecationWarning(Warning)
     |  Base class for warnings about deprecated features.
     |  
     |  Method resolution order:
     |      DeprecationWarning
     |      Warning
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class EOFError(Exception)
     |  Read beyond end of file.
     |  
     |  Method resolution order:
     |      EOFError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    EnvironmentError = class OSError(Exception)
     |  Base class for I/O related errors.
     |  
     |  Method resolution order:
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class Exception(BaseException)
     |  Common base class for all non-exit exceptions.
     |  
     |  Method resolution order:
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class FileExistsError(OSError)
     |  File already exists.
     |  
     |  Method resolution order:
     |      FileExistsError
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from OSError:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from OSError:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class FileNotFoundError(OSError)
     |  File not found.
     |  
     |  Method resolution order:
     |      FileNotFoundError
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from OSError:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from OSError:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class FloatingPointError(ArithmeticError)
     |  Floating point operation failed.
     |  
     |  Method resolution order:
     |      FloatingPointError
     |      ArithmeticError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class FutureWarning(Warning)
     |  Base class for warnings about constructs that will change semantically
     |  in the future.
     |  
     |  Method resolution order:
     |      FutureWarning
     |      Warning
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class GeneratorExit(BaseException)
     |  Request that a generator exit.
     |  
     |  Method resolution order:
     |      GeneratorExit
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    IOError = class OSError(Exception)
     |  Base class for I/O related errors.
     |  
     |  Method resolution order:
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class ImportError(Exception)
     |  Import can't find module, or can't find name in module.
     |  
     |  Method resolution order:
     |      ImportError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  msg
     |      exception message
     |  
     |  name
     |      module name
     |  
     |  path
     |      module path
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Exception:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class ImportWarning(Warning)
     |  Base class for warnings about probable mistakes in module imports
     |  
     |  Method resolution order:
     |      ImportWarning
     |      Warning
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class IndentationError(SyntaxError)
     |  Improper indentation.
     |  
     |  Method resolution order:
     |      IndentationError
     |      SyntaxError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from SyntaxError:
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from SyntaxError:
     |  
     |  filename
     |      exception filename
     |  
     |  lineno
     |      exception lineno
     |  
     |  msg
     |      exception msg
     |  
     |  offset
     |      exception offset
     |  
     |  print_file_and_line
     |      exception print_file_and_line
     |  
     |  text
     |      exception text
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Exception:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class IndexError(LookupError)
     |  Sequence index out of range.
     |  
     |  Method resolution order:
     |      IndexError
     |      LookupError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class InterruptedError(OSError)
     |  Interrupted by signal.
     |  
     |  Method resolution order:
     |      InterruptedError
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from OSError:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from OSError:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class IsADirectoryError(OSError)
     |  Operation doesn't work on directories.
     |  
     |  Method resolution order:
     |      IsADirectoryError
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from OSError:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from OSError:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class KeyError(LookupError)
     |  Mapping key not found.
     |  
     |  Method resolution order:
     |      KeyError
     |      LookupError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from LookupError:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class KeyboardInterrupt(BaseException)
     |  Program interrupted by user.
     |  
     |  Method resolution order:
     |      KeyboardInterrupt
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class LookupError(Exception)
     |  Base class for lookup errors.
     |  
     |  Method resolution order:
     |      LookupError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class MemoryError(Exception)
     |  Out of memory.
     |  
     |  Method resolution order:
     |      MemoryError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class ModuleNotFoundError(ImportError)
     |  Module not found.
     |  
     |  Method resolution order:
     |      ModuleNotFoundError
     |      ImportError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from ImportError:
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from ImportError:
     |  
     |  msg
     |      exception message
     |  
     |  name
     |      module name
     |  
     |  path
     |      module path
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Exception:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class NameError(Exception)
     |  Name not found globally.
     |  
     |  Method resolution order:
     |      NameError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class NotADirectoryError(OSError)
     |  Operation only works on directories.
     |  
     |  Method resolution order:
     |      NotADirectoryError
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from OSError:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from OSError:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class NotImplementedError(RuntimeError)
     |  Method or function hasn't been implemented yet.
     |  
     |  Method resolution order:
     |      NotImplementedError
     |      RuntimeError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class OSError(Exception)
     |  Base class for I/O related errors.
     |  
     |  Method resolution order:
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class OverflowError(ArithmeticError)
     |  Result too large to be represented.
     |  
     |  Method resolution order:
     |      OverflowError
     |      ArithmeticError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class PendingDeprecationWarning(Warning)
     |  Base class for warnings about features which will be deprecated
     |  in the future.
     |  
     |  Method resolution order:
     |      PendingDeprecationWarning
     |      Warning
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class PermissionError(OSError)
     |  Not enough permissions.
     |  
     |  Method resolution order:
     |      PermissionError
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from OSError:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from OSError:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class ProcessLookupError(OSError)
     |  Process not found.
     |  
     |  Method resolution order:
     |      ProcessLookupError
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from OSError:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from OSError:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class RecursionError(RuntimeError)
     |  Recursion limit exceeded.
     |  
     |  Method resolution order:
     |      RecursionError
     |      RuntimeError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class ReferenceError(Exception)
     |  Weak ref proxy used after referent went away.
     |  
     |  Method resolution order:
     |      ReferenceError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class ResourceWarning(Warning)
     |  Base class for warnings about resource usage.
     |  
     |  Method resolution order:
     |      ResourceWarning
     |      Warning
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class RuntimeError(Exception)
     |  Unspecified run-time error.
     |  
     |  Method resolution order:
     |      RuntimeError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class RuntimeWarning(Warning)
     |  Base class for warnings about dubious runtime behavior.
     |  
     |  Method resolution order:
     |      RuntimeWarning
     |      Warning
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class StopAsyncIteration(Exception)
     |  Signal the end from iterator.__anext__().
     |  
     |  Method resolution order:
     |      StopAsyncIteration
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class StopIteration(Exception)
     |  Signal the end from iterator.__next__().
     |  
     |  Method resolution order:
     |      StopIteration
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  value
     |      generator return value
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Exception:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class SyntaxError(Exception)
     |  Invalid syntax.
     |  
     |  Method resolution order:
     |      SyntaxError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  filename
     |      exception filename
     |  
     |  lineno
     |      exception lineno
     |  
     |  msg
     |      exception msg
     |  
     |  offset
     |      exception offset
     |  
     |  print_file_and_line
     |      exception print_file_and_line
     |  
     |  text
     |      exception text
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Exception:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class SyntaxWarning(Warning)
     |  Base class for warnings about dubious syntax.
     |  
     |  Method resolution order:
     |      SyntaxWarning
     |      Warning
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class SystemError(Exception)
     |  Internal error in the Python interpreter.
     |  
     |  Please report this to the Python maintainer, along with the traceback,
     |  the Python version, and the hardware/OS platform and version.
     |  
     |  Method resolution order:
     |      SystemError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class SystemExit(BaseException)
     |  Request to exit from the interpreter.
     |  
     |  Method resolution order:
     |      SystemExit
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  code
     |      exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class TabError(IndentationError)
     |  Improper mixture of spaces and tabs.
     |  
     |  Method resolution order:
     |      TabError
     |      IndentationError
     |      SyntaxError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from SyntaxError:
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from SyntaxError:
     |  
     |  filename
     |      exception filename
     |  
     |  lineno
     |      exception lineno
     |  
     |  msg
     |      exception msg
     |  
     |  offset
     |      exception offset
     |  
     |  print_file_and_line
     |      exception print_file_and_line
     |  
     |  text
     |      exception text
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Exception:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class TimeoutError(OSError)
     |  Timeout expired.
     |  
     |  Method resolution order:
     |      TimeoutError
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from OSError:
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from OSError:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class TypeError(Exception)
     |  Inappropriate argument type.
     |  
     |  Method resolution order:
     |      TypeError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class UnboundLocalError(NameError)
     |  Local name referenced but not bound to a value.
     |  
     |  Method resolution order:
     |      UnboundLocalError
     |      NameError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class UnicodeDecodeError(UnicodeError)
     |  Unicode decoding error.
     |  
     |  Method resolution order:
     |      UnicodeDecodeError
     |      UnicodeError
     |      ValueError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  encoding
     |      exception encoding
     |  
     |  end
     |      exception end
     |  
     |  object
     |      exception object
     |  
     |  reason
     |      exception reason
     |  
     |  start
     |      exception start
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class UnicodeEncodeError(UnicodeError)
     |  Unicode encoding error.
     |  
     |  Method resolution order:
     |      UnicodeEncodeError
     |      UnicodeError
     |      ValueError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  encoding
     |      exception encoding
     |  
     |  end
     |      exception end
     |  
     |  object
     |      exception object
     |  
     |  reason
     |      exception reason
     |  
     |  start
     |      exception start
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class UnicodeError(ValueError)
     |  Unicode related error.
     |  
     |  Method resolution order:
     |      UnicodeError
     |      ValueError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class UnicodeTranslateError(UnicodeError)
     |  Unicode translation error.
     |  
     |  Method resolution order:
     |      UnicodeTranslateError
     |      UnicodeError
     |      ValueError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  encoding
     |      exception encoding
     |  
     |  end
     |      exception end
     |  
     |  object
     |      exception object
     |  
     |  reason
     |      exception reason
     |  
     |  start
     |      exception start
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class UnicodeWarning(Warning)
     |  Base class for warnings about Unicode related problems, mostly
     |  related to conversion problems.
     |  
     |  Method resolution order:
     |      UnicodeWarning
     |      Warning
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class UserWarning(Warning)
     |  Base class for warnings generated by user code.
     |  
     |  Method resolution order:
     |      UserWarning
     |      Warning
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class ValueError(Exception)
     |  Inappropriate argument value (of correct type).
     |  
     |  Method resolution order:
     |      ValueError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class Warning(Exception)
     |  Base class for warning categories.
     |  
     |  Method resolution order:
     |      Warning
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    WindowsError = class OSError(Exception)
     |  Base class for I/O related errors.
     |  
     |  Method resolution order:
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class ZeroDivisionError(ArithmeticError)
     |  Second argument to a division or modulo operation was zero.
     |  
     |  Method resolution order:
     |      ZeroDivisionError
     |      ArithmeticError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class bool(int)
     |  bool(x) -> bool
     |  
     |  Returns True when the argument x is true, False otherwise.
     |  The builtins True and False are the only two instances of the class bool.
     |  The class bool is a subclass of the class int, and cannot be subclassed.
     |  
     |  Method resolution order:
     |      bool
     |      int
     |      object
     |  
     |  Methods defined here:
     |  
     |  __and__(self, value, /)
     |      Return self&value.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __or__(self, value, /)
     |      Return self|value.
     |  
     |  __rand__(self, value, /)
     |      Return value&self.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __ror__(self, value, /)
     |      Return value|self.
     |  
     |  __rxor__(self, value, /)
     |      Return value^self.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __xor__(self, value, /)
     |      Return self^value.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from int:
     |  
     |  __abs__(self, /)
     |      abs(self)
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __bool__(self, /)
     |      self != 0
     |  
     |  __ceil__(...)
     |      Ceiling of an Integral returns itself.
     |  
     |  __divmod__(self, value, /)
     |      Return divmod(self, value).
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __float__(self, /)
     |      float(self)
     |  
     |  __floor__(...)
     |      Flooring an Integral returns itself.
     |  
     |  __floordiv__(self, value, /)
     |      Return self//value.
     |  
     |  __format__(...)
     |      default object formatter
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __index__(self, /)
     |      Return self converted to an integer, if self is suitable for use as an index into a list.
     |  
     |  __int__(self, /)
     |      int(self)
     |  
     |  __invert__(self, /)
     |      ~self
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lshift__(self, value, /)
     |      Return self<<value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mod__(self, value, /)
     |      Return self%value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __neg__(self, /)
     |      -self
     |  
     |  __pos__(self, /)
     |      +self
     |  
     |  __pow__(self, value, mod=None, /)
     |      Return pow(self, value, mod).
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __rdivmod__(self, value, /)
     |      Return divmod(value, self).
     |  
     |  __rfloordiv__(self, value, /)
     |      Return value//self.
     |  
     |  __rlshift__(self, value, /)
     |      Return value<<self.
     |  
     |  __rmod__(self, value, /)
     |      Return value%self.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __round__(...)
     |      Rounding an Integral returns itself.
     |      Rounding with an ndigits argument also returns an integer.
     |  
     |  __rpow__(self, value, mod=None, /)
     |      Return pow(value, self, mod).
     |  
     |  __rrshift__(self, value, /)
     |      Return value>>self.
     |  
     |  __rshift__(self, value, /)
     |      Return self>>value.
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __rtruediv__(self, value, /)
     |      Return value/self.
     |  
     |  __sizeof__(...)
     |      Returns size in memory, in bytes
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  __truediv__(self, value, /)
     |      Return self/value.
     |  
     |  __trunc__(...)
     |      Truncating an Integral returns itself.
     |  
     |  bit_length(...)
     |      int.bit_length() -> int
     |      
     |      Number of bits necessary to represent self in binary.
     |      >>> bin(37)
     |      '0b100101'
     |      >>> (37).bit_length()
     |      6
     |  
     |  conjugate(...)
     |      Returns self, the complex conjugate of any int.
     |  
     |  from_bytes(...) from type
     |      int.from_bytes(bytes, byteorder, *, signed=False) -> int
     |      
     |      Return the integer represented by the given array of bytes.
     |      
     |      The bytes argument must be a bytes-like object (e.g. bytes or bytearray).
     |      
     |      The byteorder argument determines the byte order used to represent the
     |      integer.  If byteorder is 'big', the most significant byte is at the
     |      beginning of the byte array.  If byteorder is 'little', the most
     |      significant byte is at the end of the byte array.  To request the native
     |      byte order of the host system, use `sys.byteorder' as the byte order value.
     |      
     |      The signed keyword-only argument indicates whether two's complement is
     |      used to represent the integer.
     |  
     |  to_bytes(...)
     |      int.to_bytes(length, byteorder, *, signed=False) -> bytes
     |      
     |      Return an array of bytes representing an integer.
     |      
     |      The integer is represented using length bytes.  An OverflowError is
     |      raised if the integer is not representable with the given number of
     |      bytes.
     |      
     |      The byteorder argument determines the byte order used to represent the
     |      integer.  If byteorder is 'big', the most significant byte is at the
     |      beginning of the byte array.  If byteorder is 'little', the most
     |      significant byte is at the end of the byte array.  To request the native
     |      byte order of the host system, use `sys.byteorder' as the byte order value.
     |      
     |      The signed keyword-only argument determines whether two's complement is
     |      used to represent the integer.  If signed is False and a negative integer
     |      is given, an OverflowError is raised.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from int:
     |  
     |  denominator
     |      the denominator of a rational number in lowest terms
     |  
     |  imag
     |      the imaginary part of a complex number
     |  
     |  numerator
     |      the numerator of a rational number in lowest terms
     |  
     |  real
     |      the real part of a complex number
    
    class bytearray(object)
     |  bytearray(iterable_of_ints) -> bytearray
     |  bytearray(string, encoding[, errors]) -> bytearray
     |  bytearray(bytes_or_buffer) -> mutable copy of bytes_or_buffer
     |  bytearray(int) -> bytes array of size given by the parameter initialized with null bytes
     |  bytearray() -> empty bytes array
     |  
     |  Construct a mutable bytearray object from:
     |    - an iterable yielding integers in range(256)
     |    - a text string encoded using the specified encoding
     |    - a bytes or a buffer object
     |    - any object implementing the buffer API.
     |    - an integer
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __alloc__(...)
     |      B.__alloc__() -> int
     |      
     |      Return the number of bytes actually allocated.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __delitem__(self, key, /)
     |      Delete self[key].
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __iadd__(self, value, /)
     |      Implement self+=value.
     |  
     |  __imul__(self, value, /)
     |      Implement self*=value.
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mod__(self, value, /)
     |      Return self%value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.n
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(self, /)
     |      Return state information for pickling.
     |  
     |  __reduce_ex__(self, proto=0, /)
     |      Return state information for pickling.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rmod__(self, value, /)
     |      Return value%self.
     |  
     |  __rmul__(self, value, /)
     |      Return self*value.
     |  
     |  __setitem__(self, key, value, /)
     |      Set self[key] to value.
     |  
     |  __sizeof__(self, /)
     |      Returns the size of the bytearray object in memory, in bytes.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  append(self, item, /)
     |      Append a single item to the end of the bytearray.
     |      
     |      item
     |        The item to be appended.
     |  
     |  capitalize(...)
     |      B.capitalize() -> copy of B
     |      
     |      Return a copy of B with only its first character capitalized (ASCII)
     |      and the rest lower-cased.
     |  
     |  center(...)
     |      B.center(width[, fillchar]) -> copy of B
     |      
     |      Return B centered in a string of length width.  Padding is
     |      done using the specified fill character (default is a space).
     |  
     |  clear(self, /)
     |      Remove all items from the bytearray.
     |  
     |  copy(self, /)
     |      Return a copy of B.
     |  
     |  count(...)
     |      B.count(sub[, start[, end]]) -> int
     |      
     |      Return the number of non-overlapping occurrences of subsection sub in
     |      bytes B[start:end].  Optional arguments start and end are interpreted
     |      as in slice notation.
     |  
     |  decode(self, /, encoding='utf-8', errors='strict')
     |      Decode the bytearray using the codec registered for encoding.
     |      
     |      encoding
     |        The encoding with which to decode the bytearray.
     |      errors
     |        The error handling scheme to use for the handling of decoding errors.
     |        The default is 'strict' meaning that decoding errors raise a
     |        UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
     |        as well as any other name registered with codecs.register_error that
     |        can handle UnicodeDecodeErrors.
     |  
     |  endswith(...)
     |      B.endswith(suffix[, start[, end]]) -> bool
     |      
     |      Return True if B ends with the specified suffix, False otherwise.
     |      With optional start, test B beginning at that position.
     |      With optional end, stop comparing B at that position.
     |      suffix can also be a tuple of bytes to try.
     |  
     |  expandtabs(...)
     |      B.expandtabs(tabsize=8) -> copy of B
     |      
     |      Return a copy of B where all tab characters are expanded using spaces.
     |      If tabsize is not given, a tab size of 8 characters is assumed.
     |  
     |  extend(self, iterable_of_ints, /)
     |      Append all the items from the iterator or sequence to the end of the bytearray.
     |      
     |      iterable_of_ints
     |        The iterable of items to append.
     |  
     |  find(...)
     |      B.find(sub[, start[, end]]) -> int
     |      
     |      Return the lowest index in B where subsection sub is found,
     |      such that sub is contained within B[start,end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Return -1 on failure.
     |  
     |  fromhex(string, /) from type
     |      Create a bytearray object from a string of hexadecimal numbers.
     |      
     |      Spaces between two numbers are accepted.
     |      Example: bytearray.fromhex('B9 01EF') -> bytearray(b'\\xb9\\x01\\xef')
     |  
     |  hex(...)
     |      B.hex() -> string
     |      
     |      Create a string of hexadecimal numbers from a bytearray object.
     |      Example: bytearray([0xb9, 0x01, 0xef]).hex() -> 'b901ef'.
     |  
     |  index(...)
     |      B.index(sub[, start[, end]]) -> int
     |      
     |      Return the lowest index in B where subsection sub is found,
     |      such that sub is contained within B[start,end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Raises ValueError when the subsection is not found.
     |  
     |  insert(self, index, item, /)
     |      Insert a single item into the bytearray before the given index.
     |      
     |      index
     |        The index where the value is to be inserted.
     |      item
     |        The item to be inserted.
     |  
     |  isalnum(...)
     |      B.isalnum() -> bool
     |      
     |      Return True if all characters in B are alphanumeric
     |      and there is at least one character in B, False otherwise.
     |  
     |  isalpha(...)
     |      B.isalpha() -> bool
     |      
     |      Return True if all characters in B are alphabetic
     |      and there is at least one character in B, False otherwise.
     |  
     |  isdigit(...)
     |      B.isdigit() -> bool
     |      
     |      Return True if all characters in B are digits
     |      and there is at least one character in B, False otherwise.
     |  
     |  islower(...)
     |      B.islower() -> bool
     |      
     |      Return True if all cased characters in B are lowercase and there is
     |      at least one cased character in B, False otherwise.
     |  
     |  isspace(...)
     |      B.isspace() -> bool
     |      
     |      Return True if all characters in B are whitespace
     |      and there is at least one character in B, False otherwise.
     |  
     |  istitle(...)
     |      B.istitle() -> bool
     |      
     |      Return True if B is a titlecased string and there is at least one
     |      character in B, i.e. uppercase characters may only follow uncased
     |      characters and lowercase characters only cased ones. Return False
     |      otherwise.
     |  
     |  isupper(...)
     |      B.isupper() -> bool
     |      
     |      Return True if all cased characters in B are uppercase and there is
     |      at least one cased character in B, False otherwise.
     |  
     |  join(self, iterable_of_bytes, /)
     |      Concatenate any number of bytes/bytearray objects.
     |      
     |      The bytearray whose method is called is inserted in between each pair.
     |      
     |      The result is returned as a new bytearray object.
     |  
     |  ljust(...)
     |      B.ljust(width[, fillchar]) -> copy of B
     |      
     |      Return B left justified in a string of length width. Padding is
     |      done using the specified fill character (default is a space).
     |  
     |  lower(...)
     |      B.lower() -> copy of B
     |      
     |      Return a copy of B with all ASCII characters converted to lowercase.
     |  
     |  lstrip(self, bytes=None, /)
     |      Strip leading bytes contained in the argument.
     |      
     |      If the argument is omitted or None, strip leading ASCII whitespace.
     |  
     |  partition(self, sep, /)
     |      Partition the bytearray into three parts using the given separator.
     |      
     |      This will search for the separator sep in the bytearray. If the separator is
     |      found, returns a 3-tuple containing the part before the separator, the
     |      separator itself, and the part after it as new bytearray objects.
     |      
     |      If the separator is not found, returns a 3-tuple containing the copy of the
     |      original bytearray object and two empty bytearray objects.
     |  
     |  pop(self, index=-1, /)
     |      Remove and return a single item from B.
     |      
     |        index
     |          The index from where to remove the item.
     |          -1 (the default value) means remove the last item.
     |      
     |      If no index argument is given, will pop the last item.
     |  
     |  remove(self, value, /)
     |      Remove the first occurrence of a value in the bytearray.
     |      
     |      value
     |        The value to remove.
     |  
     |  replace(self, old, new, count=-1, /)
     |      Return a copy with all occurrences of substring old replaced by new.
     |      
     |        count
     |          Maximum number of occurrences to replace.
     |          -1 (the default value) means replace all occurrences.
     |      
     |      If the optional argument count is given, only the first count occurrences are
     |      replaced.
     |  
     |  reverse(self, /)
     |      Reverse the order of the values in B in place.
     |  
     |  rfind(...)
     |      B.rfind(sub[, start[, end]]) -> int
     |      
     |      Return the highest index in B where subsection sub is found,
     |      such that sub is contained within B[start,end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Return -1 on failure.
     |  
     |  rindex(...)
     |      B.rindex(sub[, start[, end]]) -> int
     |      
     |      Return the highest index in B where subsection sub is found,
     |      such that sub is contained within B[start,end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Raise ValueError when the subsection is not found.
     |  
     |  rjust(...)
     |      B.rjust(width[, fillchar]) -> copy of B
     |      
     |      Return B right justified in a string of length width. Padding is
     |      done using the specified fill character (default is a space)
     |  
     |  rpartition(self, sep, /)
     |      Partition the bytearray into three parts using the given separator.
     |      
     |      This will search for the separator sep in the bytearray, starting at the end.
     |      If the separator is found, returns a 3-tuple containing the part before the
     |      separator, the separator itself, and the part after it as new bytearray
     |      objects.
     |      
     |      If the separator is not found, returns a 3-tuple containing two empty bytearray
     |      objects and the copy of the original bytearray object.
     |  
     |  rsplit(self, /, sep=None, maxsplit=-1)
     |      Return a list of the sections in the bytearray, using sep as the delimiter.
     |      
     |        sep
     |          The delimiter according which to split the bytearray.
     |          None (the default value) means split on ASCII whitespace characters
     |          (space, tab, return, newline, formfeed, vertical tab).
     |        maxsplit
     |          Maximum number of splits to do.
     |          -1 (the default value) means no limit.
     |      
     |      Splitting is done starting at the end of the bytearray and working to the front.
     |  
     |  rstrip(self, bytes=None, /)
     |      Strip trailing bytes contained in the argument.
     |      
     |      If the argument is omitted or None, strip trailing ASCII whitespace.
     |  
     |  split(self, /, sep=None, maxsplit=-1)
     |      Return a list of the sections in the bytearray, using sep as the delimiter.
     |      
     |      sep
     |        The delimiter according which to split the bytearray.
     |        None (the default value) means split on ASCII whitespace characters
     |        (space, tab, return, newline, formfeed, vertical tab).
     |      maxsplit
     |        Maximum number of splits to do.
     |        -1 (the default value) means no limit.
     |  
     |  splitlines(self, /, keepends=False)
     |      Return a list of the lines in the bytearray, breaking at line boundaries.
     |      
     |      Line breaks are not included in the resulting list unless keepends is given and
     |      true.
     |  
     |  startswith(...)
     |      B.startswith(prefix[, start[, end]]) -> bool
     |      
     |      Return True if B starts with the specified prefix, False otherwise.
     |      With optional start, test B beginning at that position.
     |      With optional end, stop comparing B at that position.
     |      prefix can also be a tuple of bytes to try.
     |  
     |  strip(self, bytes=None, /)
     |      Strip leading and trailing bytes contained in the argument.
     |      
     |      If the argument is omitted or None, strip leading and trailing ASCII whitespace.
     |  
     |  swapcase(...)
     |      B.swapcase() -> copy of B
     |      
     |      Return a copy of B with uppercase ASCII characters converted
     |      to lowercase ASCII and vice versa.
     |  
     |  title(...)
     |      B.title() -> copy of B
     |      
     |      Return a titlecased version of B, i.e. ASCII words start with uppercase
     |      characters, all remaining cased characters have lowercase.
     |  
     |  translate(self, table, /, delete=b'')
     |      Return a copy with each character mapped by the given translation table.
     |      
     |        table
     |          Translation table, which must be a bytes object of length 256.
     |      
     |      All characters occurring in the optional argument delete are removed.
     |      The remaining characters are mapped through the given translation table.
     |  
     |  upper(...)
     |      B.upper() -> copy of B
     |      
     |      Return a copy of B with all ASCII characters converted to uppercase.
     |  
     |  zfill(...)
     |      B.zfill(width) -> copy of B
     |      
     |      Pad a numeric string B with zeros on the left, to fill a field
     |      of the specified width.  B is never truncated.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  maketrans(frm, to, /)
     |      Return a translation table useable for the bytes or bytearray translate method.
     |      
     |      The returned table will be one where each byte in frm is mapped to the byte at
     |      the same position in to.
     |      
     |      The bytes objects frm and to must be of the same length.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __hash__ = None
    
    class bytes(object)
     |  bytes(iterable_of_ints) -> bytes
     |  bytes(string, encoding[, errors]) -> bytes
     |  bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
     |  bytes(int) -> bytes object of size given by the parameter initialized with null bytes
     |  bytes() -> empty bytes object
     |  
     |  Construct an immutable array of bytes from:
     |    - an iterable yielding integers in range(256)
     |    - a text string encoded using the specified encoding
     |    - any object implementing the buffer API.
     |    - an integer
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mod__(self, value, /)
     |      Return self%value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.n
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rmod__(self, value, /)
     |      Return value%self.
     |  
     |  __rmul__(self, value, /)
     |      Return self*value.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  capitalize(...)
     |      B.capitalize() -> copy of B
     |      
     |      Return a copy of B with only its first character capitalized (ASCII)
     |      and the rest lower-cased.
     |  
     |  center(...)
     |      B.center(width[, fillchar]) -> copy of B
     |      
     |      Return B centered in a string of length width.  Padding is
     |      done using the specified fill character (default is a space).
     |  
     |  count(...)
     |      B.count(sub[, start[, end]]) -> int
     |      
     |      Return the number of non-overlapping occurrences of subsection sub in
     |      bytes B[start:end].  Optional arguments start and end are interpreted
     |      as in slice notation.
     |  
     |  decode(self, /, encoding='utf-8', errors='strict')
     |      Decode the bytes using the codec registered for encoding.
     |      
     |      encoding
     |        The encoding with which to decode the bytes.
     |      errors
     |        The error handling scheme to use for the handling of decoding errors.
     |        The default is 'strict' meaning that decoding errors raise a
     |        UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
     |        as well as any other name registered with codecs.register_error that
     |        can handle UnicodeDecodeErrors.
     |  
     |  endswith(...)
     |      B.endswith(suffix[, start[, end]]) -> bool
     |      
     |      Return True if B ends with the specified suffix, False otherwise.
     |      With optional start, test B beginning at that position.
     |      With optional end, stop comparing B at that position.
     |      suffix can also be a tuple of bytes to try.
     |  
     |  expandtabs(...)
     |      B.expandtabs(tabsize=8) -> copy of B
     |      
     |      Return a copy of B where all tab characters are expanded using spaces.
     |      If tabsize is not given, a tab size of 8 characters is assumed.
     |  
     |  find(...)
     |      B.find(sub[, start[, end]]) -> int
     |      
     |      Return the lowest index in B where subsection sub is found,
     |      such that sub is contained within B[start,end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Return -1 on failure.
     |  
     |  fromhex(string, /) from type
     |      Create a bytes object from a string of hexadecimal numbers.
     |      
     |      Spaces between two numbers are accepted.
     |      Example: bytes.fromhex('B9 01EF') -> b'\\xb9\\x01\\xef'.
     |  
     |  hex(...)
     |      B.hex() -> string
     |      
     |      Create a string of hexadecimal numbers from a bytes object.
     |      Example: b'\xb9\x01\xef'.hex() -> 'b901ef'.
     |  
     |  index(...)
     |      B.index(sub[, start[, end]]) -> int
     |      
     |      Return the lowest index in B where subsection sub is found,
     |      such that sub is contained within B[start,end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Raises ValueError when the subsection is not found.
     |  
     |  isalnum(...)
     |      B.isalnum() -> bool
     |      
     |      Return True if all characters in B are alphanumeric
     |      and there is at least one character in B, False otherwise.
     |  
     |  isalpha(...)
     |      B.isalpha() -> bool
     |      
     |      Return True if all characters in B are alphabetic
     |      and there is at least one character in B, False otherwise.
     |  
     |  isdigit(...)
     |      B.isdigit() -> bool
     |      
     |      Return True if all characters in B are digits
     |      and there is at least one character in B, False otherwise.
     |  
     |  islower(...)
     |      B.islower() -> bool
     |      
     |      Return True if all cased characters in B are lowercase and there is
     |      at least one cased character in B, False otherwise.
     |  
     |  isspace(...)
     |      B.isspace() -> bool
     |      
     |      Return True if all characters in B are whitespace
     |      and there is at least one character in B, False otherwise.
     |  
     |  istitle(...)
     |      B.istitle() -> bool
     |      
     |      Return True if B is a titlecased string and there is at least one
     |      character in B, i.e. uppercase characters may only follow uncased
     |      characters and lowercase characters only cased ones. Return False
     |      otherwise.
     |  
     |  isupper(...)
     |      B.isupper() -> bool
     |      
     |      Return True if all cased characters in B are uppercase and there is
     |      at least one cased character in B, False otherwise.
     |  
     |  join(self, iterable_of_bytes, /)
     |      Concatenate any number of bytes objects.
     |      
     |      The bytes whose method is called is inserted in between each pair.
     |      
     |      The result is returned as a new bytes object.
     |      
     |      Example: b'.'.join([b'ab', b'pq', b'rs']) -> b'ab.pq.rs'.
     |  
     |  ljust(...)
     |      B.ljust(width[, fillchar]) -> copy of B
     |      
     |      Return B left justified in a string of length width. Padding is
     |      done using the specified fill character (default is a space).
     |  
     |  lower(...)
     |      B.lower() -> copy of B
     |      
     |      Return a copy of B with all ASCII characters converted to lowercase.
     |  
     |  lstrip(self, bytes=None, /)
     |      Strip leading bytes contained in the argument.
     |      
     |      If the argument is omitted or None, strip leading  ASCII whitespace.
     |  
     |  partition(self, sep, /)
     |      Partition the bytes into three parts using the given separator.
     |      
     |      This will search for the separator sep in the bytes. If the separator is found,
     |      returns a 3-tuple containing the part before the separator, the separator
     |      itself, and the part after it.
     |      
     |      If the separator is not found, returns a 3-tuple containing the original bytes
     |      object and two empty bytes objects.
     |  
     |  replace(self, old, new, count=-1, /)
     |      Return a copy with all occurrences of substring old replaced by new.
     |      
     |        count
     |          Maximum number of occurrences to replace.
     |          -1 (the default value) means replace all occurrences.
     |      
     |      If the optional argument count is given, only the first count occurrences are
     |      replaced.
     |  
     |  rfind(...)
     |      B.rfind(sub[, start[, end]]) -> int
     |      
     |      Return the highest index in B where subsection sub is found,
     |      such that sub is contained within B[start,end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Return -1 on failure.
     |  
     |  rindex(...)
     |      B.rindex(sub[, start[, end]]) -> int
     |      
     |      Return the highest index in B where subsection sub is found,
     |      such that sub is contained within B[start,end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Raise ValueError when the subsection is not found.
     |  
     |  rjust(...)
     |      B.rjust(width[, fillchar]) -> copy of B
     |      
     |      Return B right justified in a string of length width. Padding is
     |      done using the specified fill character (default is a space)
     |  
     |  rpartition(self, sep, /)
     |      Partition the bytes into three parts using the given separator.
     |      
     |      This will search for the separator sep in the bytes, starting at the end. If
     |      the separator is found, returns a 3-tuple containing the part before the
     |      separator, the separator itself, and the part after it.
     |      
     |      If the separator is not found, returns a 3-tuple containing two empty bytes
     |      objects and the original bytes object.
     |  
     |  rsplit(self, /, sep=None, maxsplit=-1)
     |      Return a list of the sections in the bytes, using sep as the delimiter.
     |      
     |        sep
     |          The delimiter according which to split the bytes.
     |          None (the default value) means split on ASCII whitespace characters
     |          (space, tab, return, newline, formfeed, vertical tab).
     |        maxsplit
     |          Maximum number of splits to do.
     |          -1 (the default value) means no limit.
     |      
     |      Splitting is done starting at the end of the bytes and working to the front.
     |  
     |  rstrip(self, bytes=None, /)
     |      Strip trailing bytes contained in the argument.
     |      
     |      If the argument is omitted or None, strip trailing ASCII whitespace.
     |  
     |  split(self, /, sep=None, maxsplit=-1)
     |      Return a list of the sections in the bytes, using sep as the delimiter.
     |      
     |      sep
     |        The delimiter according which to split the bytes.
     |        None (the default value) means split on ASCII whitespace characters
     |        (space, tab, return, newline, formfeed, vertical tab).
     |      maxsplit
     |        Maximum number of splits to do.
     |        -1 (the default value) means no limit.
     |  
     |  splitlines(self, /, keepends=False)
     |      Return a list of the lines in the bytes, breaking at line boundaries.
     |      
     |      Line breaks are not included in the resulting list unless keepends is given and
     |      true.
     |  
     |  startswith(...)
     |      B.startswith(prefix[, start[, end]]) -> bool
     |      
     |      Return True if B starts with the specified prefix, False otherwise.
     |      With optional start, test B beginning at that position.
     |      With optional end, stop comparing B at that position.
     |      prefix can also be a tuple of bytes to try.
     |  
     |  strip(self, bytes=None, /)
     |      Strip leading and trailing bytes contained in the argument.
     |      
     |      If the argument is omitted or None, strip leading and trailing ASCII whitespace.
     |  
     |  swapcase(...)
     |      B.swapcase() -> copy of B
     |      
     |      Return a copy of B with uppercase ASCII characters converted
     |      to lowercase ASCII and vice versa.
     |  
     |  title(...)
     |      B.title() -> copy of B
     |      
     |      Return a titlecased version of B, i.e. ASCII words start with uppercase
     |      characters, all remaining cased characters have lowercase.
     |  
     |  translate(self, table, /, delete=b'')
     |      Return a copy with each character mapped by the given translation table.
     |      
     |        table
     |          Translation table, which must be a bytes object of length 256.
     |      
     |      All characters occurring in the optional argument delete are removed.
     |      The remaining characters are mapped through the given translation table.
     |  
     |  upper(...)
     |      B.upper() -> copy of B
     |      
     |      Return a copy of B with all ASCII characters converted to uppercase.
     |  
     |  zfill(...)
     |      B.zfill(width) -> copy of B
     |      
     |      Pad a numeric string B with zeros on the left, to fill a field
     |      of the specified width.  B is never truncated.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  maketrans(frm, to, /)
     |      Return a translation table useable for the bytes or bytearray translate method.
     |      
     |      The returned table will be one where each byte in frm is mapped to the byte at
     |      the same position in to.
     |      
     |      The bytes objects frm and to must be of the same length.
    
    class classmethod(object)
     |  classmethod(function) -> method
     |  
     |  Convert a function to be a class method.
     |  
     |  A class method receives the class as implicit first argument,
     |  just like an instance method receives the instance.
     |  To declare a class method, use this idiom:
     |  
     |    class C:
     |        @classmethod
     |        def f(cls, arg1, arg2, ...):
     |            ...
     |  
     |  It can be called either on the class (e.g. C.f()) or on an instance
     |  (e.g. C().f()).  The instance is ignored except for its class.
     |  If a class method is called for a derived class, the derived class
     |  object is passed as the implied first argument.
     |  
     |  Class methods are different than C++ or Java static methods.
     |  If you want those, see the staticmethod builtin.
     |  
     |  Methods defined here:
     |  
     |  __get__(self, instance, owner, /)
     |      Return an attribute of instance, which is of type owner.
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |  
     |  __func__
     |  
     |  __isabstractmethod__
    
    class complex(object)
     |  complex(real[, imag]) -> complex number
     |  
     |  Create a complex number from a real part and an optional imaginary part.
     |  This is equivalent to (real + imag*1j) where imag defaults to 0.
     |  
     |  Methods defined here:
     |  
     |  __abs__(self, /)
     |      abs(self)
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __bool__(self, /)
     |      self != 0
     |  
     |  __divmod__(self, value, /)
     |      Return divmod(self, value).
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __float__(self, /)
     |      float(self)
     |  
     |  __floordiv__(self, value, /)
     |      Return self//value.
     |  
     |  __format__(...)
     |      complex.__format__() -> str
     |      
     |      Convert to a string according to format_spec.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __int__(self, /)
     |      int(self)
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mod__(self, value, /)
     |      Return self%value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __neg__(self, /)
     |      -self
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __pos__(self, /)
     |      +self
     |  
     |  __pow__(self, value, mod=None, /)
     |      Return pow(self, value, mod).
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __rdivmod__(self, value, /)
     |      Return divmod(value, self).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rfloordiv__(self, value, /)
     |      Return value//self.
     |  
     |  __rmod__(self, value, /)
     |      Return value%self.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __rpow__(self, value, mod=None, /)
     |      Return pow(value, self, mod).
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __rtruediv__(self, value, /)
     |      Return value/self.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  __truediv__(self, value, /)
     |      Return self/value.
     |  
     |  conjugate(...)
     |      complex.conjugate() -> complex
     |      
     |      Return the complex conjugate of its argument. (3-4j).conjugate() == 3+4j.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  imag
     |      the imaginary part of a complex number
     |  
     |  real
     |      the real part of a complex number
    
    class dict(object)
     |  dict() -> new empty dictionary
     |  dict(mapping) -> new dictionary initialized from a mapping object's
     |      (key, value) pairs
     |  dict(iterable) -> new dictionary initialized as if via:
     |      d = {}
     |      for k, v in iterable:
     |          d[k] = v
     |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
     |      in the keyword argument list.  For example:  dict(one=1, two=2)
     |  
     |  Methods defined here:
     |  
     |  __contains__(self, key, /)
     |      True if D has a key k, else False.
     |  
     |  __delitem__(self, key, /)
     |      Delete self[key].
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(...)
     |      x.__getitem__(y) <==> x[y]
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setitem__(self, key, value, /)
     |      Set self[key] to value.
     |  
     |  __sizeof__(...)
     |      D.__sizeof__() -> size of D in memory, in bytes
     |  
     |  clear(...)
     |      D.clear() -> None.  Remove all items from D.
     |  
     |  copy(...)
     |      D.copy() -> a shallow copy of D
     |  
     |  fromkeys(iterable, value=None, /) from type
     |      Returns a new dict with keys from iterable and values equal to value.
     |  
     |  get(...)
     |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
     |  
     |  items(...)
     |      D.items() -> a set-like object providing a view on D's items
     |  
     |  keys(...)
     |      D.keys() -> a set-like object providing a view on D's keys
     |  
     |  pop(...)
     |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
     |      If key is not found, d is returned if given, otherwise KeyError is raised
     |  
     |  popitem(...)
     |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
     |      2-tuple; but raise KeyError if D is empty.
     |  
     |  setdefault(...)
     |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
     |  
     |  update(...)
     |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
     |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
     |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
     |      In either case, this is followed by: for k in F:  D[k] = F[k]
     |  
     |  values(...)
     |      D.values() -> an object providing a view on D's values
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __hash__ = None
    
    class enumerate(object)
     |  enumerate(iterable[, start]) -> iterator for index, value of iterable
     |  
     |  Return an enumerate object.  iterable must be another object that supports
     |  iteration.  The enumerate object yields pairs containing a count (from
     |  start, which defaults to zero) and a value yielded by the iterable argument.
     |  enumerate is useful for obtaining an indexed list:
     |      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
     |  
     |  Methods defined here:
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __next__(self, /)
     |      Implement next(self).
     |  
     |  __reduce__(...)
     |      Return state information for pickling.
    
    class filter(object)
     |  filter(function or None, iterable) --> filter object
     |  
     |  Return an iterator yielding those items of iterable for which function(item)
     |  is true. If function is None, return the items that are true.
     |  
     |  Methods defined here:
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __next__(self, /)
     |      Implement next(self).
     |  
     |  __reduce__(...)
     |      Return state information for pickling.
    
    class float(object)
     |  float(x) -> floating point number
     |  
     |  Convert a string or number to a floating point number, if possible.
     |  
     |  Methods defined here:
     |  
     |  __abs__(self, /)
     |      abs(self)
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __bool__(self, /)
     |      self != 0
     |  
     |  __divmod__(self, value, /)
     |      Return divmod(self, value).
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __float__(self, /)
     |      float(self)
     |  
     |  __floordiv__(self, value, /)
     |      Return self//value.
     |  
     |  __format__(...)
     |      float.__format__(format_spec) -> string
     |      
     |      Formats the float according to format_spec.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getformat__(...) from type
     |      float.__getformat__(typestr) -> string
     |      
     |      You probably don't want to use this function.  It exists mainly to be
     |      used in Python's test suite.
     |      
     |      typestr must be 'double' or 'float'.  This function returns whichever of
     |      'unknown', 'IEEE, big-endian' or 'IEEE, little-endian' best describes the
     |      format of floating point numbers used by the C type named by typestr.
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __int__(self, /)
     |      int(self)
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mod__(self, value, /)
     |      Return self%value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __neg__(self, /)
     |      -self
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __pos__(self, /)
     |      +self
     |  
     |  __pow__(self, value, mod=None, /)
     |      Return pow(self, value, mod).
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __rdivmod__(self, value, /)
     |      Return divmod(value, self).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rfloordiv__(self, value, /)
     |      Return value//self.
     |  
     |  __rmod__(self, value, /)
     |      Return value%self.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __round__(...)
     |      Return the Integral closest to x, rounding half toward even.
     |      When an argument is passed, work like built-in round(x, ndigits).
     |  
     |  __rpow__(self, value, mod=None, /)
     |      Return pow(value, self, mod).
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __rtruediv__(self, value, /)
     |      Return value/self.
     |  
     |  __setformat__(...) from type
     |      float.__setformat__(typestr, fmt) -> None
     |      
     |      You probably don't want to use this function.  It exists mainly to be
     |      used in Python's test suite.
     |      
     |      typestr must be 'double' or 'float'.  fmt must be one of 'unknown',
     |      'IEEE, big-endian' or 'IEEE, little-endian', and in addition can only be
     |      one of the latter two if it appears to match the underlying C reality.
     |      
     |      Override the automatic determination of C-level floating point type.
     |      This affects how floats are converted to and from binary strings.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  __truediv__(self, value, /)
     |      Return self/value.
     |  
     |  __trunc__(...)
     |      Return the Integral closest to x between 0 and x.
     |  
     |  as_integer_ratio(...)
     |      float.as_integer_ratio() -> (int, int)
     |      
     |      Return a pair of integers, whose ratio is exactly equal to the original
     |      float and with a positive denominator.
     |      Raise OverflowError on infinities and a ValueError on NaNs.
     |      
     |      >>> (10.0).as_integer_ratio()
     |      (10, 1)
     |      >>> (0.0).as_integer_ratio()
     |      (0, 1)
     |      >>> (-.25).as_integer_ratio()
     |      (-1, 4)
     |  
     |  conjugate(...)
     |      Return self, the complex conjugate of any float.
     |  
     |  fromhex(...) from type
     |      float.fromhex(string) -> float
     |      
     |      Create a floating-point number from a hexadecimal string.
     |      >>> float.fromhex('0x1.ffffp10')
     |      2047.984375
     |      >>> float.fromhex('-0x1p-1074')
     |      -5e-324
     |  
     |  hex(...)
     |      float.hex() -> string
     |      
     |      Return a hexadecimal representation of a floating-point number.
     |      >>> (-0.1).hex()
     |      '-0x1.999999999999ap-4'
     |      >>> 3.14159.hex()
     |      '0x1.921f9f01b866ep+1'
     |  
     |  is_integer(...)
     |      Return True if the float is an integer.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  imag
     |      the imaginary part of a complex number
     |  
     |  real
     |      the real part of a complex number
    
    class frozenset(object)
     |  frozenset() -> empty frozenset object
     |  frozenset(iterable) -> frozenset object
     |  
     |  Build an immutable unordered collection of unique elements.
     |  
     |  Methods defined here:
     |  
     |  __and__(self, value, /)
     |      Return self&value.
     |  
     |  __contains__(...)
     |      x.__contains__(y) <==> y in x.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __or__(self, value, /)
     |      Return self|value.
     |  
     |  __rand__(self, value, /)
     |      Return value&self.
     |  
     |  __reduce__(...)
     |      Return state information for pickling.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __ror__(self, value, /)
     |      Return value|self.
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __rxor__(self, value, /)
     |      Return value^self.
     |  
     |  __sizeof__(...)
     |      S.__sizeof__() -> size of S in memory, in bytes
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  __xor__(self, value, /)
     |      Return self^value.
     |  
     |  copy(...)
     |      Return a shallow copy of a set.
     |  
     |  difference(...)
     |      Return the difference of two or more sets as a new set.
     |      
     |      (i.e. all elements that are in this set but not the others.)
     |  
     |  intersection(...)
     |      Return the intersection of two sets as a new set.
     |      
     |      (i.e. all elements that are in both sets.)
     |  
     |  isdisjoint(...)
     |      Return True if two sets have a null intersection.
     |  
     |  issubset(...)
     |      Report whether another set contains this set.
     |  
     |  issuperset(...)
     |      Report whether this set contains another set.
     |  
     |  symmetric_difference(...)
     |      Return the symmetric difference of two sets as a new set.
     |      
     |      (i.e. all elements that are in exactly one of the sets.)
     |  
     |  union(...)
     |      Return the union of sets as a new set.
     |      
     |      (i.e. all elements that are in either set.)
    
    class int(object)
     |  int(x=0) -> integer
     |  int(x, base=10) -> integer
     |  
     |  Convert a number or string to an integer, or return 0 if no arguments
     |  are given.  If x is a number, return x.__int__().  For floating point
     |  numbers, this truncates towards zero.
     |  
     |  If x is not a number or if base is given, then x must be a string,
     |  bytes, or bytearray instance representing an integer literal in the
     |  given base.  The literal can be preceded by '+' or '-' and be surrounded
     |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
     |  Base 0 means to interpret the base from the string as an integer literal.
     |  >>> int('0b100', base=0)
     |  4
     |  
     |  Methods defined here:
     |  
     |  __abs__(self, /)
     |      abs(self)
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __and__(self, value, /)
     |      Return self&value.
     |  
     |  __bool__(self, /)
     |      self != 0
     |  
     |  __ceil__(...)
     |      Ceiling of an Integral returns itself.
     |  
     |  __divmod__(self, value, /)
     |      Return divmod(self, value).
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __float__(self, /)
     |      float(self)
     |  
     |  __floor__(...)
     |      Flooring an Integral returns itself.
     |  
     |  __floordiv__(self, value, /)
     |      Return self//value.
     |  
     |  __format__(...)
     |      default object formatter
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __index__(self, /)
     |      Return self converted to an integer, if self is suitable for use as an index into a list.
     |  
     |  __int__(self, /)
     |      int(self)
     |  
     |  __invert__(self, /)
     |      ~self
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lshift__(self, value, /)
     |      Return self<<value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mod__(self, value, /)
     |      Return self%value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __neg__(self, /)
     |      -self
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __or__(self, value, /)
     |      Return self|value.
     |  
     |  __pos__(self, /)
     |      +self
     |  
     |  __pow__(self, value, mod=None, /)
     |      Return pow(self, value, mod).
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __rand__(self, value, /)
     |      Return value&self.
     |  
     |  __rdivmod__(self, value, /)
     |      Return divmod(value, self).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rfloordiv__(self, value, /)
     |      Return value//self.
     |  
     |  __rlshift__(self, value, /)
     |      Return value<<self.
     |  
     |  __rmod__(self, value, /)
     |      Return value%self.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __ror__(self, value, /)
     |      Return value|self.
     |  
     |  __round__(...)
     |      Rounding an Integral returns itself.
     |      Rounding with an ndigits argument also returns an integer.
     |  
     |  __rpow__(self, value, mod=None, /)
     |      Return pow(value, self, mod).
     |  
     |  __rrshift__(self, value, /)
     |      Return value>>self.
     |  
     |  __rshift__(self, value, /)
     |      Return self>>value.
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __rtruediv__(self, value, /)
     |      Return value/self.
     |  
     |  __rxor__(self, value, /)
     |      Return value^self.
     |  
     |  __sizeof__(...)
     |      Returns size in memory, in bytes
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  __truediv__(self, value, /)
     |      Return self/value.
     |  
     |  __trunc__(...)
     |      Truncating an Integral returns itself.
     |  
     |  __xor__(self, value, /)
     |      Return self^value.
     |  
     |  bit_length(...)
     |      int.bit_length() -> int
     |      
     |      Number of bits necessary to represent self in binary.
     |      >>> bin(37)
     |      '0b100101'
     |      >>> (37).bit_length()
     |      6
     |  
     |  conjugate(...)
     |      Returns self, the complex conjugate of any int.
     |  
     |  from_bytes(...) from type
     |      int.from_bytes(bytes, byteorder, *, signed=False) -> int
     |      
     |      Return the integer represented by the given array of bytes.
     |      
     |      The bytes argument must be a bytes-like object (e.g. bytes or bytearray).
     |      
     |      The byteorder argument determines the byte order used to represent the
     |      integer.  If byteorder is 'big', the most significant byte is at the
     |      beginning of the byte array.  If byteorder is 'little', the most
     |      significant byte is at the end of the byte array.  To request the native
     |      byte order of the host system, use `sys.byteorder' as the byte order value.
     |      
     |      The signed keyword-only argument indicates whether two's complement is
     |      used to represent the integer.
     |  
     |  to_bytes(...)
     |      int.to_bytes(length, byteorder, *, signed=False) -> bytes
     |      
     |      Return an array of bytes representing an integer.
     |      
     |      The integer is represented using length bytes.  An OverflowError is
     |      raised if the integer is not representable with the given number of
     |      bytes.
     |      
     |      The byteorder argument determines the byte order used to represent the
     |      integer.  If byteorder is 'big', the most significant byte is at the
     |      beginning of the byte array.  If byteorder is 'little', the most
     |      significant byte is at the end of the byte array.  To request the native
     |      byte order of the host system, use `sys.byteorder' as the byte order value.
     |      
     |      The signed keyword-only argument determines whether two's complement is
     |      used to represent the integer.  If signed is False and a negative integer
     |      is given, an OverflowError is raised.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  denominator
     |      the denominator of a rational number in lowest terms
     |  
     |  imag
     |      the imaginary part of a complex number
     |  
     |  numerator
     |      the numerator of a rational number in lowest terms
     |  
     |  real
     |      the real part of a complex number
    
    class list(object)
     |  list() -> new empty list
     |  list(iterable) -> new list initialized from iterable's items
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __delitem__(self, key, /)
     |      Delete self[key].
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(...)
     |      x.__getitem__(y) <==> x[y]
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __iadd__(self, value, /)
     |      Implement self+=value.
     |  
     |  __imul__(self, value, /)
     |      Implement self*=value.
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.n
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __reversed__(...)
     |      L.__reversed__() -- return a reverse iterator over the list
     |  
     |  __rmul__(self, value, /)
     |      Return self*value.
     |  
     |  __setitem__(self, key, value, /)
     |      Set self[key] to value.
     |  
     |  __sizeof__(...)
     |      L.__sizeof__() -- size of L in memory, in bytes
     |  
     |  append(...)
     |      L.append(object) -> None -- append object to end
     |  
     |  clear(...)
     |      L.clear() -> None -- remove all items from L
     |  
     |  copy(...)
     |      L.copy() -> list -- a shallow copy of L
     |  
     |  count(...)
     |      L.count(value) -> integer -- return number of occurrences of value
     |  
     |  extend(...)
     |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
     |  
     |  index(...)
     |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
     |      Raises ValueError if the value is not present.
     |  
     |  insert(...)
     |      L.insert(index, object) -- insert object before index
     |  
     |  pop(...)
     |      L.pop([index]) -> item -- remove and return item at index (default last).
     |      Raises IndexError if list is empty or index is out of range.
     |  
     |  remove(...)
     |      L.remove(value) -> None -- remove first occurrence of value.
     |      Raises ValueError if the value is not present.
     |  
     |  reverse(...)
     |      L.reverse() -- reverse *IN PLACE*
     |  
     |  sort(...)
     |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __hash__ = None
    
    class map(object)
     |  map(func, *iterables) --> map object
     |  
     |  Make an iterator that computes the function using arguments from
     |  each of the iterables.  Stops when the shortest iterable is exhausted.
     |  
     |  Methods defined here:
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __next__(self, /)
     |      Implement next(self).
     |  
     |  __reduce__(...)
     |      Return state information for pickling.
    
    class memoryview(object)
     |  Create a new memoryview object which references the given object.
     |  
     |  Methods defined here:
     |  
     |  __delitem__(self, key, /)
     |      Delete self[key].
     |  
     |  __enter__(...)
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __exit__(...)
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setitem__(self, key, value, /)
     |      Set self[key] to value.
     |  
     |  cast(self, /, format, *, shape)
     |      Cast a memoryview to a new format or shape.
     |  
     |  hex(self, /)
     |      Return the data in the buffer as a string of hexadecimal numbers.
     |  
     |  release(self, /)
     |      Release the underlying buffer exposed by the memoryview object.
     |  
     |  tobytes(self, /)
     |      Return the data in the buffer as a byte string.
     |  
     |  tolist(self, /)
     |      Return the data in the buffer as a list of elements.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  c_contiguous
     |      A bool indicating whether the memory is C contiguous.
     |  
     |  contiguous
     |      A bool indicating whether the memory is contiguous.
     |  
     |  f_contiguous
     |      A bool indicating whether the memory is Fortran contiguous.
     |  
     |  format
     |      A string containing the format (in struct module style)
     |      for each element in the view.
     |  
     |  itemsize
     |      The size in bytes of each element of the memoryview.
     |  
     |  nbytes
     |      The amount of space in bytes that the array would use in
     |      a contiguous representation.
     |  
     |  ndim
     |      An integer indicating how many dimensions of a multi-dimensional
     |      array the memory represents.
     |  
     |  obj
     |      The underlying object of the memoryview.
     |  
     |  readonly
     |      A bool indicating whether the memory is read only.
     |  
     |  shape
     |      A tuple of ndim integers giving the shape of the memory
     |      as an N-dimensional array.
     |  
     |  strides
     |      A tuple of ndim integers giving the size in bytes to access
     |      each element for each dimension of the array.
     |  
     |  suboffsets
     |      A tuple of integers used internally for PIL-style arrays.
    
    class object
     |  The most base type
    
    class property(object)
     |  property(fget=None, fset=None, fdel=None, doc=None) -> property attribute
     |  
     |  fget is a function to be used for getting an attribute value, and likewise
     |  fset is a function for setting, and fdel a function for del'ing, an
     |  attribute.  Typical use is to define a managed attribute x:
     |  
     |  class C(object):
     |      def getx(self): return self._x
     |      def setx(self, value): self._x = value
     |      def delx(self): del self._x
     |      x = property(getx, setx, delx, "I'm the 'x' property.")
     |  
     |  Decorators make defining new properties or modifying existing ones easy:
     |  
     |  class C(object):
     |      @property
     |      def x(self):
     |          "I am the 'x' property."
     |          return self._x
     |      @x.setter
     |      def x(self, value):
     |          self._x = value
     |      @x.deleter
     |      def x(self):
     |          del self._x
     |  
     |  Methods defined here:
     |  
     |  __delete__(self, instance, /)
     |      Delete an attribute of instance.
     |  
     |  __get__(self, instance, owner, /)
     |      Return an attribute of instance, which is of type owner.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __set__(self, instance, value, /)
     |      Set an attribute of instance to value.
     |  
     |  deleter(...)
     |      Descriptor to change the deleter on a property.
     |  
     |  getter(...)
     |      Descriptor to change the getter on a property.
     |  
     |  setter(...)
     |      Descriptor to change the setter on a property.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __isabstractmethod__
     |  
     |  fdel
     |  
     |  fget
     |  
     |  fset
    
    class range(object)
     |  range(stop) -> range object
     |  range(start, stop[, step]) -> range object
     |  
     |  Return an object that produces a sequence of integers from start (inclusive)
     |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
     |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
     |  These are exactly the valid indices for a list of 4 elements.
     |  When step is given, it specifies the increment (or decrement).
     |  
     |  Methods defined here:
     |  
     |  __bool__(self, /)
     |      self != 0
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __reversed__(...)
     |      Return a reverse iterator.
     |  
     |  count(...)
     |      rangeobject.count(value) -> integer -- return number of occurrences of value
     |  
     |  index(...)
     |      rangeobject.index(value, [start, [stop]]) -> integer -- return index of value.
     |      Raise ValueError if the value is not present.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  start
     |  
     |  step
     |  
     |  stop
    
    class reversed(object)
     |  reversed(sequence) -> reverse iterator over values of the sequence
     |  
     |  Return a reverse iterator
     |  
     |  Methods defined here:
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __length_hint__(...)
     |      Private method returning an estimate of len(list(it)).
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __next__(self, /)
     |      Implement next(self).
     |  
     |  __reduce__(...)
     |      Return state information for pickling.
     |  
     |  __setstate__(...)
     |      Set state information for unpickling.
    
    class set(object)
     |  set() -> new empty set object
     |  set(iterable) -> new set object
     |  
     |  Build an unordered collection of unique elements.
     |  
     |  Methods defined here:
     |  
     |  __and__(self, value, /)
     |      Return self&value.
     |  
     |  __contains__(...)
     |      x.__contains__(y) <==> y in x.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __iand__(self, value, /)
     |      Return self&=value.
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __ior__(self, value, /)
     |      Return self|=value.
     |  
     |  __isub__(self, value, /)
     |      Return self-=value.
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __ixor__(self, value, /)
     |      Return self^=value.
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __or__(self, value, /)
     |      Return self|value.
     |  
     |  __rand__(self, value, /)
     |      Return value&self.
     |  
     |  __reduce__(...)
     |      Return state information for pickling.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __ror__(self, value, /)
     |      Return value|self.
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __rxor__(self, value, /)
     |      Return value^self.
     |  
     |  __sizeof__(...)
     |      S.__sizeof__() -> size of S in memory, in bytes
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  __xor__(self, value, /)
     |      Return self^value.
     |  
     |  add(...)
     |      Add an element to a set.
     |      
     |      This has no effect if the element is already present.
     |  
     |  clear(...)
     |      Remove all elements from this set.
     |  
     |  copy(...)
     |      Return a shallow copy of a set.
     |  
     |  difference(...)
     |      Return the difference of two or more sets as a new set.
     |      
     |      (i.e. all elements that are in this set but not the others.)
     |  
     |  difference_update(...)
     |      Remove all elements of another set from this set.
     |  
     |  discard(...)
     |      Remove an element from a set if it is a member.
     |      
     |      If the element is not a member, do nothing.
     |  
     |  intersection(...)
     |      Return the intersection of two sets as a new set.
     |      
     |      (i.e. all elements that are in both sets.)
     |  
     |  intersection_update(...)
     |      Update a set with the intersection of itself and another.
     |  
     |  isdisjoint(...)
     |      Return True if two sets have a null intersection.
     |  
     |  issubset(...)
     |      Report whether another set contains this set.
     |  
     |  issuperset(...)
     |      Report whether this set contains another set.
     |  
     |  pop(...)
     |      Remove and return an arbitrary set element.
     |      Raises KeyError if the set is empty.
     |  
     |  remove(...)
     |      Remove an element from a set; it must be a member.
     |      
     |      If the element is not a member, raise a KeyError.
     |  
     |  symmetric_difference(...)
     |      Return the symmetric difference of two sets as a new set.
     |      
     |      (i.e. all elements that are in exactly one of the sets.)
     |  
     |  symmetric_difference_update(...)
     |      Update a set with the symmetric difference of itself and another.
     |  
     |  union(...)
     |      Return the union of sets as a new set.
     |      
     |      (i.e. all elements that are in either set.)
     |  
     |  update(...)
     |      Update a set with the union of itself and others.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __hash__ = None
    
    class slice(object)
     |  slice(stop)
     |  slice(start, stop[, step])
     |  
     |  Create a slice object.  This is used for extended slicing (e.g. a[0:10:2]).
     |  
     |  Methods defined here:
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      Return state information for pickling.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  indices(...)
     |      S.indices(len) -> (start, stop, stride)
     |      
     |      Assuming a sequence of length len, calculate the start and stop
     |      indices, and the stride length of the extended slice described by
     |      S. Out of bounds indices are clipped in a manner consistent with the
     |      handling of normal slices.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  start
     |  
     |  step
     |  
     |  stop
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __hash__ = None
    
    class staticmethod(object)
     |  staticmethod(function) -> method
     |  
     |  Convert a function to be a static method.
     |  
     |  A static method does not receive an implicit first argument.
     |  To declare a static method, use this idiom:
     |  
     |       class C:
     |           @staticmethod
     |           def f(arg1, arg2, ...):
     |               ...
     |  
     |  It can be called either on the class (e.g. C.f()) or on an instance
     |  (e.g. C().f()).  The instance is ignored except for its class.
     |  
     |  Static methods in Python are similar to those found in Java or C++.
     |  For a more advanced concept, see the classmethod builtin.
     |  
     |  Methods defined here:
     |  
     |  __get__(self, instance, owner, /)
     |      Return an attribute of instance, which is of type owner.
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |  
     |  __func__
     |  
     |  __isabstractmethod__
    
    class str(object)
     |  str(object='') -> str
     |  str(bytes_or_buffer[, encoding[, errors]]) -> str
     |  
     |  Create a new string object from the given object. If encoding or
     |  errors is specified, then the object must expose a data buffer
     |  that will be decoded using the given encoding and error handler.
     |  Otherwise, returns the result of object.__str__() (if defined)
     |  or repr(object).
     |  encoding defaults to sys.getdefaultencoding().
     |  errors defaults to 'strict'.
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __format__(...)
     |      S.__format__(format_spec) -> str
     |      
     |      Return a formatted version of S as described by format_spec.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mod__(self, value, /)
     |      Return self%value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.n
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rmod__(self, value, /)
     |      Return value%self.
     |  
     |  __rmul__(self, value, /)
     |      Return self*value.
     |  
     |  __sizeof__(...)
     |      S.__sizeof__() -> size of S in memory, in bytes
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  capitalize(...)
     |      S.capitalize() -> str
     |      
     |      Return a capitalized version of S, i.e. make the first character
     |      have upper case and the rest lower case.
     |  
     |  casefold(...)
     |      S.casefold() -> str
     |      
     |      Return a version of S suitable for caseless comparisons.
     |  
     |  center(...)
     |      S.center(width[, fillchar]) -> str
     |      
     |      Return S centered in a string of length width. Padding is
     |      done using the specified fill character (default is a space)
     |  
     |  count(...)
     |      S.count(sub[, start[, end]]) -> int
     |      
     |      Return the number of non-overlapping occurrences of substring sub in
     |      string S[start:end].  Optional arguments start and end are
     |      interpreted as in slice notation.
     |  
     |  encode(...)
     |      S.encode(encoding='utf-8', errors='strict') -> bytes
     |      
     |      Encode S using the codec registered for encoding. Default encoding
     |      is 'utf-8'. errors may be given to set a different error
     |      handling scheme. Default is 'strict' meaning that encoding errors raise
     |      a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
     |      'xmlcharrefreplace' as well as any other name registered with
     |      codecs.register_error that can handle UnicodeEncodeErrors.
     |  
     |  endswith(...)
     |      S.endswith(suffix[, start[, end]]) -> bool
     |      
     |      Return True if S ends with the specified suffix, False otherwise.
     |      With optional start, test S beginning at that position.
     |      With optional end, stop comparing S at that position.
     |      suffix can also be a tuple of strings to try.
     |  
     |  expandtabs(...)
     |      S.expandtabs(tabsize=8) -> str
     |      
     |      Return a copy of S where all tab characters are expanded using spaces.
     |      If tabsize is not given, a tab size of 8 characters is assumed.
     |  
     |  find(...)
     |      S.find(sub[, start[, end]]) -> int
     |      
     |      Return the lowest index in S where substring sub is found,
     |      such that sub is contained within S[start:end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Return -1 on failure.
     |  
     |  format(...)
     |      S.format(*args, **kwargs) -> str
     |      
     |      Return a formatted version of S, using substitutions from args and kwargs.
     |      The substitutions are identified by braces ('{' and '}').
     |  
     |  format_map(...)
     |      S.format_map(mapping) -> str
     |      
     |      Return a formatted version of S, using substitutions from mapping.
     |      The substitutions are identified by braces ('{' and '}').
     |  
     |  index(...)
     |      S.index(sub[, start[, end]]) -> int
     |      
     |      Return the lowest index in S where substring sub is found, 
     |      such that sub is contained within S[start:end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Raises ValueError when the substring is not found.
     |  
     |  isalnum(...)
     |      S.isalnum() -> bool
     |      
     |      Return True if all characters in S are alphanumeric
     |      and there is at least one character in S, False otherwise.
     |  
     |  isalpha(...)
     |      S.isalpha() -> bool
     |      
     |      Return True if all characters in S are alphabetic
     |      and there is at least one character in S, False otherwise.
     |  
     |  isdecimal(...)
     |      S.isdecimal() -> bool
     |      
     |      Return True if there are only decimal characters in S,
     |      False otherwise.
     |  
     |  isdigit(...)
     |      S.isdigit() -> bool
     |      
     |      Return True if all characters in S are digits
     |      and there is at least one character in S, False otherwise.
     |  
     |  isidentifier(...)
     |      S.isidentifier() -> bool
     |      
     |      Return True if S is a valid identifier according
     |      to the language definition.
     |      
     |      Use keyword.iskeyword() to test for reserved identifiers
     |      such as "def" and "class".
     |  
     |  islower(...)
     |      S.islower() -> bool
     |      
     |      Return True if all cased characters in S are lowercase and there is
     |      at least one cased character in S, False otherwise.
     |  
     |  isnumeric(...)
     |      S.isnumeric() -> bool
     |      
     |      Return True if there are only numeric characters in S,
     |      False otherwise.
     |  
     |  isprintable(...)
     |      S.isprintable() -> bool
     |      
     |      Return True if all characters in S are considered
     |      printable in repr() or S is empty, False otherwise.
     |  
     |  isspace(...)
     |      S.isspace() -> bool
     |      
     |      Return True if all characters in S are whitespace
     |      and there is at least one character in S, False otherwise.
     |  
     |  istitle(...)
     |      S.istitle() -> bool
     |      
     |      Return True if S is a titlecased string and there is at least one
     |      character in S, i.e. upper- and titlecase characters may only
     |      follow uncased characters and lowercase characters only cased ones.
     |      Return False otherwise.
     |  
     |  isupper(...)
     |      S.isupper() -> bool
     |      
     |      Return True if all cased characters in S are uppercase and there is
     |      at least one cased character in S, False otherwise.
     |  
     |  join(...)
     |      S.join(iterable) -> str
     |      
     |      Return a string which is the concatenation of the strings in the
     |      iterable.  The separator between elements is S.
     |  
     |  ljust(...)
     |      S.ljust(width[, fillchar]) -> str
     |      
     |      Return S left-justified in a Unicode string of length width. Padding is
     |      done using the specified fill character (default is a space).
     |  
     |  lower(...)
     |      S.lower() -> str
     |      
     |      Return a copy of the string S converted to lowercase.
     |  
     |  lstrip(...)
     |      S.lstrip([chars]) -> str
     |      
     |      Return a copy of the string S with leading whitespace removed.
     |      If chars is given and not None, remove characters in chars instead.
     |  
     |  partition(...)
     |      S.partition(sep) -> (head, sep, tail)
     |      
     |      Search for the separator sep in S, and return the part before it,
     |      the separator itself, and the part after it.  If the separator is not
     |      found, return S and two empty strings.
     |  
     |  replace(...)
     |      S.replace(old, new[, count]) -> str
     |      
     |      Return a copy of S with all occurrences of substring
     |      old replaced by new.  If the optional argument count is
     |      given, only the first count occurrences are replaced.
     |  
     |  rfind(...)
     |      S.rfind(sub[, start[, end]]) -> int
     |      
     |      Return the highest index in S where substring sub is found,
     |      such that sub is contained within S[start:end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Return -1 on failure.
     |  
     |  rindex(...)
     |      S.rindex(sub[, start[, end]]) -> int
     |      
     |      Return the highest index in S where substring sub is found,
     |      such that sub is contained within S[start:end].  Optional
     |      arguments start and end are interpreted as in slice notation.
     |      
     |      Raises ValueError when the substring is not found.
     |  
     |  rjust(...)
     |      S.rjust(width[, fillchar]) -> str
     |      
     |      Return S right-justified in a string of length width. Padding is
     |      done using the specified fill character (default is a space).
     |  
     |  rpartition(...)
     |      S.rpartition(sep) -> (head, sep, tail)
     |      
     |      Search for the separator sep in S, starting at the end of S, and return
     |      the part before it, the separator itself, and the part after it.  If the
     |      separator is not found, return two empty strings and S.
     |  
     |  rsplit(...)
     |      S.rsplit(sep=None, maxsplit=-1) -> list of strings
     |      
     |      Return a list of the words in S, using sep as the
     |      delimiter string, starting at the end of the string and
     |      working to the front.  If maxsplit is given, at most maxsplit
     |      splits are done. If sep is not specified, any whitespace string
     |      is a separator.
     |  
     |  rstrip(...)
     |      S.rstrip([chars]) -> str
     |      
     |      Return a copy of the string S with trailing whitespace removed.
     |      If chars is given and not None, remove characters in chars instead.
     |  
     |  split(...)
     |      S.split(sep=None, maxsplit=-1) -> list of strings
     |      
     |      Return a list of the words in S, using sep as the
     |      delimiter string.  If maxsplit is given, at most maxsplit
     |      splits are done. If sep is not specified or is None, any
     |      whitespace string is a separator and empty strings are
     |      removed from the result.
     |  
     |  splitlines(...)
     |      S.splitlines([keepends]) -> list of strings
     |      
     |      Return a list of the lines in S, breaking at line boundaries.
     |      Line breaks are not included in the resulting list unless keepends
     |      is given and true.
     |  
     |  startswith(...)
     |      S.startswith(prefix[, start[, end]]) -> bool
     |      
     |      Return True if S starts with the specified prefix, False otherwise.
     |      With optional start, test S beginning at that position.
     |      With optional end, stop comparing S at that position.
     |      prefix can also be a tuple of strings to try.
     |  
     |  strip(...)
     |      S.strip([chars]) -> str
     |      
     |      Return a copy of the string S with leading and trailing
     |      whitespace removed.
     |      If chars is given and not None, remove characters in chars instead.
     |  
     |  swapcase(...)
     |      S.swapcase() -> str
     |      
     |      Return a copy of S with uppercase characters converted to lowercase
     |      and vice versa.
     |  
     |  title(...)
     |      S.title() -> str
     |      
     |      Return a titlecased version of S, i.e. words start with title case
     |      characters, all remaining cased characters have lower case.
     |  
     |  translate(...)
     |      S.translate(table) -> str
     |      
     |      Return a copy of the string S in which each character has been mapped
     |      through the given translation table. The table must implement
     |      lookup/indexing via __getitem__, for instance a dictionary or list,
     |      mapping Unicode ordinals to Unicode ordinals, strings, or None. If
     |      this operation raises LookupError, the character is left untouched.
     |      Characters mapped to None are deleted.
     |  
     |  upper(...)
     |      S.upper() -> str
     |      
     |      Return a copy of S converted to uppercase.
     |  
     |  zfill(...)
     |      S.zfill(width) -> str
     |      
     |      Pad a numeric string S with zeros on the left, to fill a field
     |      of the specified width. The string S is never truncated.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  maketrans(x, y=None, z=None, /)
     |      Return a translation table usable for str.translate().
     |      
     |      If there is only one argument, it must be a dictionary mapping Unicode
     |      ordinals (integers) or characters to Unicode ordinals, strings or None.
     |      Character keys will be then converted to ordinals.
     |      If there are two arguments, they must be strings of equal length, and
     |      in the resulting dictionary, each character in x will be mapped to the
     |      character at the same position in y. If there is a third argument, it
     |      must be a string, whose characters will be mapped to None in the result.
    
    class super(object)
     |  super() -> same as super(__class__, <first argument>)
     |  super(type) -> unbound super object
     |  super(type, obj) -> bound super object; requires isinstance(obj, type)
     |  super(type, type2) -> bound super object; requires issubclass(type2, type)
     |  Typical use to call a cooperative superclass method:
     |  class C(B):
     |      def meth(self, arg):
     |          super().meth(arg)
     |  This works for class methods too:
     |  class C(B):
     |      @classmethod
     |      def cmeth(cls, arg):
     |          super().cmeth(arg)
     |  
     |  Methods defined here:
     |  
     |  __get__(self, instance, owner, /)
     |      Return an attribute of instance, which is of type owner.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __self__
     |      the instance invoking super(); may be None
     |  
     |  __self_class__
     |      the type of the instance invoking super(); may be None
     |  
     |  __thisclass__
     |      the class invoking super()
    
    class tuple(object)
     |  tuple() -> empty tuple
     |  tuple(iterable) -> tuple initialized from iterable's items
     |  
     |  If the argument is a tuple, the return value is the same object.
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.n
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rmul__(self, value, /)
     |      Return self*value.
     |  
     |  count(...)
     |      T.count(value) -> integer -- return number of occurrences of value
     |  
     |  index(...)
     |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
     |      Raises ValueError if the value is not present.
    
    class type(object)
     |  type(object_or_name, bases, dict)
     |  type(object) -> the object's type
     |  type(name, bases, dict) -> a new type
     |  
     |  Methods defined here:
     |  
     |  __call__(self, /, *args, **kwargs)
     |      Call self as a function.
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __dir__(...)
     |      __dir__() -> list
     |      specialized __dir__ implementation for types
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __instancecheck__(...)
     |      __instancecheck__() -> bool
     |      check if an object is an instance
     |  
     |  __new__(*args, **kwargs)
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __prepare__(...)
     |      __prepare__() -> dict
     |      used to create the namespace for the class statement
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __sizeof__(...)
     |      __sizeof__() -> int
     |      return memory consumption of the type object
     |  
     |  __subclasscheck__(...)
     |      __subclasscheck__() -> bool
     |      check if a class is a subclass
     |  
     |  __subclasses__(...)
     |      __subclasses__() -> list of immediate subclasses
     |  
     |  mro(...)
     |      mro() -> list
     |      return a type's method resolution order
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __abstractmethods__
     |  
     |  __dict__
     |  
     |  __text_signature__
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __base__ = <class 'object'>
     |      The most base type
     |  
     |  __bases__ = (<class 'object'>,)
     |  
     |  __basicsize__ = 432
     |  
     |  __dictoffset__ = 132
     |  
     |  __flags__ = -2146675712
     |  
     |  __itemsize__ = 20
     |  
     |  __mro__ = (<class 'type'>, <class 'object'>)
     |  
     |  __weakrefoffset__ = 184
    
    class zip(object)
     |  zip(iter1 [,iter2 [...]]) --> zip object
     |  
     |  Return a zip object whose .__next__() method returns a tuple where
     |  the i-th element comes from the i-th iterable argument.  The .__next__()
     |  method continues until the shortest iterable in the argument sequence
     |  is exhausted and then it raises StopIteration.
     |  
     |  Methods defined here:
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __new__(*args, **kwargs) from type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __next__(self, /)
     |      Implement next(self).
     |  
     |  __reduce__(...)
     |      Return state information for pickling.

FUNCTIONS
    __build_class__(...)
        __build_class__(func, name, *bases, metaclass=None, **kwds) -> class
        
        Internal helper function used by the class statement.
    
    __import__(...)
        __import__(name, globals=None, locals=None, fromlist=(), level=0) -> module
        
        Import a module. Because this function is meant for use by the Python
        interpreter and not for general use it is better to use
        importlib.import_module() to programmatically import a module.
        
        The globals argument is only used to determine the context;
        they are not modified.  The locals argument is unused.  The fromlist
        should be a list of names to emulate ``from name import ...'', or an
        empty list to emulate ``import name''.
        When importing a module from a package, note that __import__('A.B', ...)
        returns package A when fromlist is empty, but its submodule B when
        fromlist is not empty.  Level is used to determine whether to perform 
        absolute or relative imports. 0 is absolute while a positive number
        is the number of parent directories to search relative to the current module.
    
    abs(x, /)
        Return the absolute value of the argument.
    
    all(iterable, /)
        Return True if bool(x) is True for all values x in the iterable.
        
        If the iterable is empty, return True.
    
    any(iterable, /)
        Return True if bool(x) is True for any x in the iterable.
        
        If the iterable is empty, return False.
    
    ascii(obj, /)
        Return an ASCII-only representation of an object.
        
        As repr(), return a string containing a printable representation of an
        object, but escape the non-ASCII characters in the string returned by
        repr() using \\x, \\u or \\U escapes. This generates a string similar
        to that returned by repr() in Python 2.
    
    bin(number, /)
        Return the binary representation of an integer.
        
        >>> bin(2796202)
        '0b1010101010101010101010'
    
    callable(obj, /)
        Return whether the object is callable (i.e., some kind of function).
        
        Note that classes are callable, as are instances of classes with a
        __call__() method.
    
    chr(i, /)
        Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
    
    compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
        Compile source into a code object that can be executed by exec() or eval().
        
        The source code may represent a Python module, statement or expression.
        The filename will be used for run-time error messages.
        The mode must be 'exec' to compile a module, 'single' to compile a
        single (interactive) statement, or 'eval' to compile an expression.
        The flags argument, if present, controls which future statements influence
        the compilation of the code.
        The dont_inherit argument, if true, stops the compilation inheriting
        the effects of any future statements in effect in the code calling
        compile; if absent or false these statements do influence the compilation,
        in addition to any features explicitly specified.
    
    delattr(obj, name, /)
        Deletes the named attribute from the given object.
        
        delattr(x, 'y') is equivalent to ``del x.y''
    
    dir(...)
        dir([object]) -> list of strings
        
        If called without an argument, return the names in the current scope.
        Else, return an alphabetized list of names comprising (some of) the attributes
        of the given object, and of attributes reachable from it.
        If the object supplies a method named __dir__, it will be used; otherwise
        the default dir() logic is used and returns:
          for a module object: the module's attributes.
          for a class object:  its attributes, and recursively the attributes
            of its bases.
          for any other object: its attributes, its class's attributes, and
            recursively the attributes of its class's base classes.
    
    divmod(x, y, /)
        Return the tuple (x//y, x%y).  Invariant: div*y + mod == x.
    
    eval(source, globals=None, locals=None, /)
        Evaluate the given source in the context of globals and locals.
        
        The source may be a string representing a Python expression
        or a code object as returned by compile().
        The globals must be a dictionary and locals can be any mapping,
        defaulting to the current globals and locals.
        If only globals is given, locals defaults to it.
    
    exec(source, globals=None, locals=None, /)
        Execute the given source in the context of globals and locals.
        
        The source may be a string representing one or more Python statements
        or a code object as returned by compile().
        The globals must be a dictionary and locals can be any mapping,
        defaulting to the current globals and locals.
        If only globals is given, locals defaults to it.
    
    format(value, format_spec='', /)
        Return value.__format__(format_spec)
        
        format_spec defaults to the empty string.
        See the Format Specification Mini-Language section of help('FORMATTING') for
        details.
    
    getattr(...)
        getattr(object, name[, default]) -> value
        
        Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
        When a default argument is given, it is returned when the attribute doesn't
        exist; without it, an exception is raised in that case.
    
    globals()
        Return the dictionary containing the current scope's global variables.
        
        NOTE: Updates to this dictionary *will* affect name lookups in the current
        global scope and vice-versa.
    
    hasattr(obj, name, /)
        Return whether the object has an attribute with the given name.
        
        This is done by calling getattr(obj, name) and catching AttributeError.
    
    hash(obj, /)
        Return the hash value for the given object.
        
        Two objects that compare equal must also have the same hash value, but the
        reverse is not necessarily true.
    
    hex(number, /)
        Return the hexadecimal representation of an integer.
        
        >>> hex(12648430)
        '0xc0ffee'
    
    id(obj, /)
        Return the identity of an object.
        
        This is guaranteed to be unique among simultaneously existing objects.
        (CPython uses the object's memory address.)
    
    input(prompt=None, /)
        Read a string from standard input.  The trailing newline is stripped.
        
        The prompt string, if given, is printed to standard output without a
        trailing newline before reading input.
        
        If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
        On *nix systems, readline is used if available.
    
    isinstance(obj, class_or_tuple, /)
        Return whether an object is an instance of a class or of a subclass thereof.
        
        A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
        check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
        or ...`` etc.
    
    issubclass(cls, class_or_tuple, /)
        Return whether 'cls' is a derived from another class or is the same class.
        
        A tuple, as in ``issubclass(x, (A, B, ...))``, may be given as the target to
        check against. This is equivalent to ``issubclass(x, A) or issubclass(x, B)
        or ...`` etc.
    
    iter(...)
        iter(iterable) -> iterator
        iter(callable, sentinel) -> iterator
        
        Get an iterator from an object.  In the first form, the argument must
        supply its own iterator, or be a sequence.
        In the second form, the callable is called until it returns the sentinel.
    
    len(obj, /)
        Return the number of items in a container.
    
    locals()
        Return a dictionary containing the current scope's local variables.
        
        NOTE: Whether or not updates to this dictionary will affect name lookups in
        the local scope and vice-versa is *implementation dependent* and not
        covered by any backwards compatibility guarantees.
    
    max(...)
        max(iterable, *[, default=obj, key=func]) -> value
        max(arg1, arg2, *args, *[, key=func]) -> value
        
        With a single iterable argument, return its biggest item. The
        default keyword-only argument specifies an object to return if
        the provided iterable is empty.
        With two or more arguments, return the largest argument.
    
    min(...)
        min(iterable, *[, default=obj, key=func]) -> value
        min(arg1, arg2, *args, *[, key=func]) -> value
        
        With a single iterable argument, return its smallest item. The
        default keyword-only argument specifies an object to return if
        the provided iterable is empty.
        With two or more arguments, return the smallest argument.
    
    next(...)
        next(iterator[, default])
        
        Return the next item from the iterator. If default is given and the iterator
        is exhausted, it is returned instead of raising StopIteration.
    
    oct(number, /)
        Return the octal representation of an integer.
        
        >>> oct(342391)
        '0o1234567'
    
    open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
        Open file and return a stream.  Raise IOError upon failure.
        
        file is either a text or byte string giving the name (and the path
        if the file isn't in the current working directory) of the file to
        be opened or an integer file descriptor of the file to be
        wrapped. (If a file descriptor is given, it is closed when the
        returned I/O object is closed, unless closefd is set to False.)
        
        mode is an optional string that specifies the mode in which the file
        is opened. It defaults to 'r' which means open for reading in text
        mode.  Other common values are 'w' for writing (truncating the file if
        it already exists), 'x' for creating and writing to a new file, and
        'a' for appending (which on some Unix systems, means that all writes
        append to the end of the file regardless of the current seek position).
        In text mode, if encoding is not specified the encoding used is platform
        dependent: locale.getpreferredencoding(False) is called to get the
        current locale encoding. (For reading and writing raw bytes use binary
        mode and leave encoding unspecified.) The available modes are:
        
        ========= ===============================================================
        Character Meaning
        --------- ---------------------------------------------------------------
        'r'       open for reading (default)
        'w'       open for writing, truncating the file first
        'x'       create a new file and open it for writing
        'a'       open for writing, appending to the end of the file if it exists
        'b'       binary mode
        't'       text mode (default)
        '+'       open a disk file for updating (reading and writing)
        'U'       universal newline mode (deprecated)
        ========= ===============================================================
        
        The default mode is 'rt' (open for reading text). For binary random
        access, the mode 'w+b' opens and truncates the file to 0 bytes, while
        'r+b' opens the file without truncation. The 'x' mode implies 'w' and
        raises an `FileExistsError` if the file already exists.
        
        Python distinguishes between files opened in binary and text modes,
        even when the underlying operating system doesn't. Files opened in
        binary mode (appending 'b' to the mode argument) return contents as
        bytes objects without any decoding. In text mode (the default, or when
        't' is appended to the mode argument), the contents of the file are
        returned as strings, the bytes having been first decoded using a
        platform-dependent encoding or using the specified encoding if given.
        
        'U' mode is deprecated and will raise an exception in future versions
        of Python.  It has no effect in Python 3.  Use newline to control
        universal newlines mode.
        
        buffering is an optional integer used to set the buffering policy.
        Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
        line buffering (only usable in text mode), and an integer > 1 to indicate
        the size of a fixed-size chunk buffer.  When no buffering argument is
        given, the default buffering policy works as follows:
        
        * Binary files are buffered in fixed-size chunks; the size of the buffer
          is chosen using a heuristic trying to determine the underlying device's
          "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
          On many systems, the buffer will typically be 4096 or 8192 bytes long.
        
        * "Interactive" text files (files for which isatty() returns True)
          use line buffering.  Other text files use the policy described above
          for binary files.
        
        encoding is the name of the encoding used to decode or encode the
        file. This should only be used in text mode. The default encoding is
        platform dependent, but any encoding supported by Python can be
        passed.  See the codecs module for the list of supported encodings.
        
        errors is an optional string that specifies how encoding errors are to
        be handled---this argument should not be used in binary mode. Pass
        'strict' to raise a ValueError exception if there is an encoding error
        (the default of None has the same effect), or pass 'ignore' to ignore
        errors. (Note that ignoring encoding errors can lead to data loss.)
        See the documentation for codecs.register or run 'help(codecs.Codec)'
        for a list of the permitted encoding error strings.
        
        newline controls how universal newlines works (it only applies to text
        mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
        follows:
        
        * On input, if newline is None, universal newlines mode is
          enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
          these are translated into '\n' before being returned to the
          caller. If it is '', universal newline mode is enabled, but line
          endings are returned to the caller untranslated. If it has any of
          the other legal values, input lines are only terminated by the given
          string, and the line ending is returned to the caller untranslated.
        
        * On output, if newline is None, any '\n' characters written are
          translated to the system default line separator, os.linesep. If
          newline is '' or '\n', no translation takes place. If newline is any
          of the other legal values, any '\n' characters written are translated
          to the given string.
        
        If closefd is False, the underlying file descriptor will be kept open
        when the file is closed. This does not work when a file name is given
        and must be True in that case.
        
        A custom opener can be used by passing a callable as *opener*. The
        underlying file descriptor for the file object is then obtained by
        calling *opener* with (*file*, *flags*). *opener* must return an open
        file descriptor (passing os.open as *opener* results in functionality
        similar to passing None).
        
        open() returns a file object whose type depends on the mode, and
        through which the standard file operations such as reading and writing
        are performed. When open() is used to open a file in a text mode ('w',
        'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
        a file in a binary mode, the returned class varies: in read binary
        mode, it returns a BufferedReader; in write binary and append binary
        modes, it returns a BufferedWriter, and in read/write mode, it returns
        a BufferedRandom.
        
        It is also possible to use a string or bytearray as a file for both
        reading and writing. For strings StringIO can be used like a file
        opened in a text mode, and for bytes a BytesIO can be used like a file
        opened in a binary mode.
    
    ord(c, /)
        Return the Unicode code point for a one-character string.
    
    pow(x, y, z=None, /)
        Equivalent to x**y (with two arguments) or x**y % z (with three arguments)
        
        Some types, such as ints, are able to use a more efficient algorithm when
        invoked using the three argument form.
    
    print(...)
        print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
        
        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.
    
    repr(obj, /)
        Return the canonical string representation of the object.
        
        For many object types, including most builtins, eval(repr(obj)) == obj.
    
    round(...)
        round(number[, ndigits]) -> number
        
        Round a number to a given precision in decimal digits (default 0 digits).
        This returns an int when called with one argument, otherwise the
        same type as the number. ndigits may be negative.
    
    setattr(obj, name, value, /)
        Sets the named attribute on the given object to the specified value.
        
        setattr(x, 'y', v) is equivalent to ``x.y = v''
    
    sorted(iterable, /, *, key=None, reverse=False)
        Return a new list containing all items from the iterable in ascending order.
        
        A custom key function can be supplied to customize the sort order, and the
        reverse flag can be set to request the result in descending order.
    
    sum(iterable, start=0, /)
        Return the sum of a 'start' value (default: 0) plus an iterable of numbers
        
        When the iterable is empty, return the start value.
        This function is intended specifically for use with numeric values and may
        reject non-numeric types.
    
    vars(...)
        vars([object]) -> dictionary
        
        Without arguments, equivalent to locals().
        With an argument, equivalent to object.__dict__.

DATA
    Ellipsis = Ellipsis
    False = False
    None = None
    NotImplemented = NotImplemented
    True = True
    __debug__ = True
    copyright = Copyright (c) 2001-2017 Python Software Foundati...ematisc...
    credits =     Thanks to CWI, CNRI, BeOpen.com, Zope Corpor...opment.  ...
    exit = Use exit() or Ctrl-Z plus Return to exit
    help = Type help() for interactive help, or help(object) for help abou...
    license = Type license() to see the full license text
    quit = Use quit() or Ctrl-Z plus Return to exit

FILE
    (built-in)


>>> dir(builtins)
							      
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> 
========== RESTART: C:/Python/Python36-32/exception_handling_001.py ==========
enter the first number5
enter the second number0
Division by zero not allowed
thanks
>>> 
============ RESTART: C:/Python/Python36-32/file handling_002.py ============
enter the first number5
enter the second number0
division by zero
Thanks
>>> 
