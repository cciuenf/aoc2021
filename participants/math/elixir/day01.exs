defmodule Day01 do
  @spec main(Path.t()) :: {integer, integer}
  def main(file_path) do
    input =
      file_path
      |> File.read!()
      |> parse_input()

    {depth_increasement(input), input |> to_sliding_window |> depth_increasement}
  end

  @spec depth_increasement(list(integer)) :: integer
  defp depth_increasement(measurements, acc \\ 0)

  defp depth_increasement([], result), do: result

  defp depth_increasement([a, b | tl], acc) when b > a,
    do: depth_increasement([b | tl], acc + 1)

  defp depth_increasement([_hd | tl], acc),
    do: depth_increasement(tl, acc)

  @spec to_sliding_window(list(integer)) :: list(integer)
  defp to_sliding_window([]), do: []

  defp to_sliding_window(measurements) do
    sum = measurements |> Enum.take(3) |> Enum.sum()

    [sum | measurements |> tl() |> to_sliding_window()]
  end

  @spec parse_input(binary) :: list(integer)
  defp parse_input(file_content) do
    file_content
    |> String.split("\n", trim: true)
    |> Enum.map(&String.to_integer/1)
  end
end

{larger_depths, larger_sums} = Day01.main("../data/day01.txt")

IO.puts("#{larger_depths} measurements are larger than the previous measurement")
IO.puts("#{larger_sums} sums are larger than the previous sum")
