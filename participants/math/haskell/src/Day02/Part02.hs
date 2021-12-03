module Day02.Part02 (getFinalPosition, productPositions) where

import Day02.Parser (Move(..))

type Unit = Int
type Aim = Int

data Position a = Horizontal a | Depth a deriving (Show)

data State = S Aim (Position Unit, Position Unit) deriving (Show)

instance Functor Position where
  fmap f (Horizontal u) = Horizontal (f u)
  fmap f (Depth u) = Depth (f u)

initState :: State
initState = S 0 (Horizontal 0, Depth 0)

doCommand :: Move -> State -> State
doCommand (Forward u) (S aim (x, y)) = S aim ((+ u) <$> x, (+ (aim * u)) <$> y)
doCommand (Down u) (S aim pos) = S (aim + u) pos
doCommand (Up u) (S aim pos) = S (aim - u) pos

getFinalPosition :: [Move] -> State
getFinalPosition = (foldr doCommand initState) . reverse

productPositions :: State -> Int
productPositions (S _ ((Horizontal x), (Depth y))) = x * y
