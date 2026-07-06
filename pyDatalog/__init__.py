# Copyright (c) 2024-2026 Magnon Compute Corporation. All Rights Reserved.


from . import version
from . import Logic
    
Logic = Logic.Logic # give easy access to the Logic class

Logic().clear() # initialize the logic in the current thread
    
