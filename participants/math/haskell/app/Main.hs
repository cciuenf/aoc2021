module Main where

import qualified Day01 as Day01
import qualified Day02 as Day02

main :: IO ()
main = do
  Day01.main Day01.dataFile
  Day02.main Day01.dataFile
