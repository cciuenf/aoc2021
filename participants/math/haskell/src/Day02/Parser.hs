module Day02.Parser (parseMoves, Move(..)) where

import Data.Char (digitToInt)

import Text.Parsec

type Parser = Parsec String ()

data Move
  = Forward Int
  | Up Int
  | Down Int
  deriving (Show)

parseForward :: Parser Move
parseForward = do
  unit <- string "forward" *> space *> digit
  return $ Forward (digitToInt unit)

parseUp :: Parser Move
parseUp = do
  unit <- string "up" *> space *> digit
  return $ Up (digitToInt unit)

parseDown :: Parser Move
parseDown = do
  unit <- string "down" *> space *> digit
  return $ Down (digitToInt unit)

parseMove :: Parser Move
parseMove = (parseForward <|> parseUp <|> parseDown) <* oneOf "\n"

parseMoves :: Parser [Move]
parseMoves = many parseMove <* eof
