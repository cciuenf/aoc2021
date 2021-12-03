module Day1 (main) where

depthIncreasement :: [Int] -> Int
depthIncreasement = length . filterNegatives . differences
  where
    differences xs = zipWith (-) xs (tail xs)
    filterNegatives = filter (< 0)

toSlidingWindow :: [Int] -> [Int]
toSlidingWindow [] = []
toSlidingWindow xs = (sum . triplet) xs : toSlidingWindow (tail xs)
  where
    triplet = take 3

main :: IO ()
main = do
    input <- map read . lines <$> readFile dataFile
    let largerDepths = depthIncreasement input
    putStrLn $ (show largerDepths) ++ " measurements are larger than the previous measurement"
    let largerSums = (depthIncreasement . toSlidingWindow) input
    putStrLn $ (show largerSums) ++ " sums are larger than the previous sum"

dataFile :: FilePath
dataFile = "../data/day01.txt"
