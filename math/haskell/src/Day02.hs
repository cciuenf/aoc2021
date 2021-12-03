module Day02 (main, dataFile) where

import qualified Day02.Part01 as Part01
import qualified Day02.Part02 as Part02
import Day02.Parser (parseMoves, Move(..))

import Text.Parsec (parse)

dataFile :: FilePath
dataFile = "../data/day02.txt"

part01 :: [Move] -> Int
part01 = Part01.productPositions . Part01.getFinalPosition

part02 :: [Move] -> Int
part02 = Part02.productPositions . Part02.getFinalPosition

teste = [Forward 5, Down 5, Forward 8, Up 3, Down 8, Forward 2]

main :: FilePath -> IO ()
main inputPath = do
  input <- readFile inputPath
  let (Right moves) = parse parseMoves "<stdio>" input
  let productPosition = part01 moves
  putStrLn $ "Product of final position: " ++ (show productPosition)
  let productPositionWithAim = part02 moves
  putStrLn $ "Product of final position with aim: " ++ (show productPositionWithAim)
