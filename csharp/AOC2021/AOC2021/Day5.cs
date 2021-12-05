namespace AOC2021
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    public static class Day5
    {
        public static void Part1()
        {
            var vents = new List<Line>();
            var maxX = 0;
            var maxY = 0;

            foreach (string line in System.IO.File.ReadLines(@"AppData\fulldata.txt"))
            {
                var (start, end, x, y) = GetPointsFromLine(line);
                vents.Add(new Line(start, end));

                maxX = Math.Max(maxX, x);
                maxY = Math.Max(maxY, y);
            }


            var board = new int[maxX +1,maxY+1];

            foreach(var vent in vents)
            {
                if (vent.Start.x == vent.End.x)
                {

                    var smaller = Math.Min(vent.Start.y, vent.End.y);
                    var larger = Math.Max(vent.Start.y, vent.End.y);

                    for (int i = smaller; i <= larger; i++)
                    {
                        board[vent.Start.x, i]++;
                    }
                }
                else if (vent.Start.y == vent.End.y)
                {
                    var smaller = Math.Min(vent.Start.x, vent.End.x);
                    var larger = Math.Max(vent.Start.x, vent.End.x);
                    for (int i = smaller; i <= larger; i++)
                    {
                        board[i, vent.Start.y]++;
                    }
                }
            }

            var count = 0;
            for(int i =0; i <= maxX; i++)
            {
                for (int j = 0; j <= maxY; j++)
                {
                    if (board[i, j] >= 2) count++;
                }
            }

            Console.WriteLine("Part 1: " + count);
        }


        public static void Part2()
        {
            var vents = new List<Line>();
            var maxX = 0;
            var maxY = 0;

            foreach (string line in System.IO.File.ReadLines(@"AppData\fulldata.txt"))
            {
                var (start, end, x, y) = GetPointsFromLine(line);
                vents.Add(new Line(start, end));

                maxX = Math.Max(maxX, x);
                maxY = Math.Max(maxY, y);
            }


            var board = new int[maxX + 1, maxY + 1];

            foreach (var vent in vents)
            {
                if (vent.Start.x == vent.End.x)
                {

                    var smaller = Math.Min(vent.Start.y, vent.End.y);
                    var larger = Math.Max(vent.Start.y, vent.End.y);

                    for (int i = smaller; i <= larger; i++)
                    {
                        board[vent.Start.x, i]++;
                    }
                }
                else if (vent.Start.y == vent.End.y)
                {
                    var smaller = Math.Min(vent.Start.x, vent.End.x);
                    var larger = Math.Max(vent.Start.x, vent.End.x);
                    for (int i = smaller; i <= larger; i++)
                    {
                        board[i, vent.Start.y]++;
                    }
                }
                else
                {
                    //good lord there must be an easier way
                    var smallerX = Math.Min(vent.Start.x, vent.End.x);
                    var largerX = Math.Max(vent.Start.x, vent.End.x);

                    var smallerY = Math.Min(vent.Start.y, vent.End.y);
                    var largerY = Math.Max(vent.Start.y, vent.End.y);

                    if (vent.Start.y > vent.End.y && vent.Start.x > vent.End.x)
                    {
                        for (int i = largerX, j = largerY; i >= smallerX && j >= smallerY; i--, j--)
                        {
                            board[i, j]++;
                        }
                    }
                    else if (vent.Start.y > vent.End.y)
                    {
                        for (int i = smallerX, j = largerY; i <= largerX && j >= smallerY; i++, j--)
                        {
                            board[i, j]++;
                        }
                    }
                    else if (vent.Start.x > vent.End.x)
                    {
                        for (int i = largerX, j = smallerY; i >= smallerX && j <= largerY; i--, j++)
                        {
                            board[i, j]++;
                        }
                    }
                    else
                    {
                        for (int i = smallerX, j = smallerY; i <= largerX && j <= largerY; i++, j++)
                        {
                            board[i, j]++;
                        }
                    }
                }
            }

            var count = 0;
            for (int i = 0; i <= maxX; i++)
            {
                for (int j = 0; j <= maxY; j++)
                {
                    if (board[i, j] >= 2) count++;
                }
            }

            Console.WriteLine("Part 2: " + count);
        }


        private static (Point, Point, int, int) GetPointsFromLine(string line)
        {
            var points = line.Split(" -> ");

            var start = points[0].Split(',');
            var end = points[1].Split(',');

            var startX = Convert.ToInt32(start[0]);
            var startY = Convert.ToInt32(start[1]);
            var endX = Convert.ToInt32(end[0]);
            var endY = Convert.ToInt32(end[1]);

            var maxX = Math.Max(startX, endX);
            var maxY = Math.Max(startY, endY);

            return (new Point(startX, startY), new Point(endX, endY), maxX, maxY);
        }
    }

    public class Line
    {
        public Point Start { get; set; }
        public Point End { get; set; }

        public Line(Point start, Point end)
        {
            this.Start = start;
            this.End = end;
        }
    }

    public class Point
    {
        public int x { get; set; }
        public int y { get; set; }

        public Point(int x, int y)
        {
            this.x = x;
            this.y = y;
        }
    }
}
