namespace AOC2021
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    public static class Day4
    {

        public static void Part1()
        {
            var orderToDraw = new List<int>();
            var isFirstLine = true;
            var newBoard = false;

            var boards = new List<Board>();
            var currentBoard = new List<List<BingoSpot>>();

            foreach (string line in System.IO.File.ReadLines(@"AppData\fulldata.txt"))
            {
                if (orderToDraw.Count() == 0)
                {
                    orderToDraw = line.Split(',').Select(x => Convert.ToInt32(x)).ToList();
                }

                if (String.IsNullOrWhiteSpace(line))
                {
                    newBoard = true;
                    if(currentBoard.Count() > 0)
                        boards.Add(new Board() { Values = currentBoard });

                    currentBoard = new List<List<BingoSpot>>();
                }
                else if(newBoard)
                {
                    currentBoard.Add(GetBingoSpots(line.Split(' ').ToList()));
                    newBoard = false;
                }
                else if(!isFirstLine)
                {
                    currentBoard.Add(GetBingoSpots(line.Split(' ').ToList()));
                }

                isFirstLine = false;
            }
            boards.Add(new Board() { Values = currentBoard });

            var drawCount = 0;

            var hasWon = false;

            foreach(var randomDraw in orderToDraw)
            {
                drawCount++;
                foreach(var board in boards)
                {
                    foreach(var i in board.Values)
                    {
                        foreach (var j in i)
                        {
                            if (j.Value == randomDraw) j.Checked = true;
                        }
                    }
                }

                if (drawCount >= 5)
                {
                    //check all boards
                    foreach (var (board, index) in boards.WithIndex())
                    {
                        var checkColumnCount = 0;
                        var checkRow = false;

                        if (hasWon) return;

                        for(int i = 0; i < board.Values.Count(); i++)
                        {
                            checkColumnCount = 0;
                            for (int j = 0; j < 5; j++)
                            {
                                if (board.Values.ElementAt(j).ElementAt(i).Checked) checkColumnCount++;
                            }

                            if (checkColumnCount == 5)
                            {
                                OutputAnswer(board, randomDraw);
                                hasWon = true;
                                return;
                            }
                        }

                        foreach (var i in board.Values)
                        {
                            checkRow = i.Where(x => x.Checked).Count() == 5;

                            if (checkRow)
                            {
                                OutputAnswer(board, randomDraw);
                                hasWon = true;
                                return;
                            }

                            checkRow = false;
                        }
                    }
                }
            }
        }

        public static IEnumerable<(T item, int index)> WithIndex<T>(this IEnumerable<T> self)
            => self.Select((item, index) => (item, index));

        private static void OutputAnswer(Board winningBoard, int winningDraw, int? part = 1)
        {
            var unmarkedNumbers = new List<int>();

            foreach (var row in winningBoard.Values)
            {
                unmarkedNumbers.AddRange(row.Where(x => !x.Checked).Select(x => x.Value));
            }

            Console.WriteLine("Part " + part+ ": " + unmarkedNumbers.Sum() * winningDraw);
        }

        private static List<BingoSpot> GetBingoSpots(List<string> values)
        {
            return values.Where(x => !string.IsNullOrWhiteSpace(x)).Select(y => new BingoSpot(Convert.ToInt32(y))).ToList();
        }

        public static void Part2()
        {
            var orderToDraw = new List<int>();
            var isFirstLine = true;
            var newBoard = false;

            var boards = new List<Board>();
            var currentBoard = new List<List<BingoSpot>>();

            foreach (string line in System.IO.File.ReadLines(@"AppData\fulldata.txt"))
            {
                if (orderToDraw.Count() == 0)
                {
                    orderToDraw = line.Split(',').Select(x => Convert.ToInt32(x)).ToList();
                }

                if (String.IsNullOrWhiteSpace(line))
                {
                    newBoard = true;
                    if (currentBoard.Count() > 0)
                        boards.Add(new Board() { Values = currentBoard, Won = false });

                    currentBoard = new List<List<BingoSpot>>();
                }
                else if (newBoard)
                {
                    currentBoard.Add(GetBingoSpots(line.Split(' ').ToList()));
                    newBoard = false;
                }
                else if (!isFirstLine)
                {
                    currentBoard.Add(GetBingoSpots(line.Split(' ').ToList()));
                }

                isFirstLine = false;
            }
            boards.Add(new Board() { Values = currentBoard });

            var winningBoardsCount = 0;
            var totalBoardsCount = boards.Count();
            var drawCount = 0;

            var lastWinningBoard = new Board();

            foreach (var randomDraw in orderToDraw)
            {
                drawCount++;
                foreach (var board in boards)
                {
                    foreach (var i in board.Values)
                    {
                        foreach (var j in i)
                        {
                            if (j.Value == randomDraw) j.Checked = true;
                        }
                    }
                }

                if (drawCount >= 5)
                {
                    //check all boards
                    foreach (var (board, index) in boards.WithIndex())
                    {
                        var checkColumnCount = 0;
                        var checkRow = false;

                        for (int i = 0; i < board.Values.Count(); i++)
                        {
                            checkColumnCount = 0;
                            for (int j = 0; j < 5; j++)
                            {
                                if (board.Values.ElementAt(j).ElementAt(i).Checked) checkColumnCount++;
                            }

                            if (checkColumnCount == 5)
                            {
                                if (!board.Won)
                                {
                                    winningBoardsCount++;
                                    lastWinningBoard = board;
                                }
                                board.Won = true;
                                break;
                            }
                        }

                        foreach (var i in board.Values)
                        {
                            checkRow = i.Where(x => x.Checked).Count() == 5;

                            if (checkRow)
                            {
                                if (!board.Won)
                                {
                                    winningBoardsCount++;
                                    lastWinningBoard = board;
                                }
                                board.Won = true;
                                break;
                            }

                            checkRow = false;
                        }
                    }
                }

                if (totalBoardsCount == winningBoardsCount)
                {
                    OutputAnswer(lastWinningBoard, randomDraw, 2);
                    return;
                }
            }



        }
    }

    public class Board
    {
        public bool Won { get; set; }
        public List<List<BingoSpot>> Values { get; set; }
    }


    public class BingoSpot
    {
        public int Value { get; set; }
        public bool Checked { get; set; }
        public BingoSpot(int value)
        {
            this.Value = value;
        }
    }
}
