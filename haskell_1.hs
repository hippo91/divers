main = do
  putStrLn "Hello you!"
  putStrLn "Enter the number you want the table of:"
  num <- getLine
  putStrLn ("Here is the table of " ++ num)
  let number = read num :: Integer
  print [number * n | n <- [1 .. 10]]
