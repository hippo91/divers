filterFromConvergenceMask :: [a] -> [Bool] -> [a]
filterFromConvergenceMask [] [] = []
filterFromConvergenceMask (val:values) (has_conv:mask)
  | has_conv == True = val : filterFromConvergenceMask values mask
  | has_conv == False = filterFromConvergenceMask values mask
