module Day02.Part01 (getFinalPosition, productPositions) where

import Day02.Parser (Move(..))

type Unit = Int

data Position = Horizontal Unit | Depth Unit

type State = (Position, Position)

initState :: State
initState = (Horizontal 0, Depth 0)

doCommand :: Move -> State -> State
doCommand (Forward u) ((Horizontal x), y) = (Horizontal (u + x), y)
doCommand (Down u) (x, (Depth y)) = (x, Depth (u + y))
doCommand (Up u) (x, (Depth y)) = (x, Depth (y - u))

getFinalPosition :: [Move] -> State
getFinalPosition = foldr doCommand initState

productPositions :: State -> Int
productPositions ((Horizontal x), (Depth y)) = x * y
