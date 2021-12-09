namespace AOC2021
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    public static class Day9
    {
        public static void Part1()
        {
            var points = new List<List<int>>();

            foreach (string line in System.IO.File.ReadLines(@"AppData\fulldata.txt"))
            {
                points.Add(line.ToCharArray().Select(x => Convert.ToInt32(x.ToString())).ToList());
            }

            var lows = new List<int>();

            for(int i = 0; i < points.Count(); i++)
            {
                for(int j = 0; j < points[i].Count(); j++)
                {
                    var currentPoint = points[i][j];
                    if(i == 0)
                    {
                        if(j == 0)
                        {
                            if (currentPoint < points[i + 1][j]
                                && currentPoint < points[i][j + 1])
                                    lows.Add(currentPoint);
                        }
                        else if (j == points[i].Count() - 1)
                        {
                            if (currentPoint < points[i+1][j]
                                && currentPoint < points[i][j-1])
                                lows.Add(currentPoint);
                        }
                        else
                        {
                            if (currentPoint < points[i + 1][j]
                                && currentPoint < points[i][j - 1]
                                && currentPoint < points[i][j + 1])
                                lows.Add(currentPoint);
                        }

                    }
                    else if(i == points.Count() - 1)
                    {
                        if (j == 0)
                        {
                            if (currentPoint < points[i - 1][j]
                                && currentPoint < points[i][j + 1])
                                lows.Add(currentPoint);
                        }
                        else if (j == points[i].Count() - 1)
                        {
                            if (currentPoint < points[i - 1][j]
                                && currentPoint < points[i][j - 1])
                                lows.Add(currentPoint);
                        }
                        else
                        {
                            if (currentPoint < points[i - 1][j]
                                && currentPoint < points[i][j - 1]
                                && currentPoint < points[i][j + 1])
                                lows.Add(currentPoint);
                        }
                    }
                    else
                    {
                        if (j == 0)
                        {
                            if (currentPoint < points[i - 1][j]
                                && currentPoint < points[i + 1][j]
                                && currentPoint < points[i][j + 1])
                                lows.Add(currentPoint);
                        }
                        else if (j == points[i].Count() - 1)
                        {
                            if (currentPoint < points[i - 1][j]
                                && currentPoint < points[i + 1][j]
                                && currentPoint < points[i][j - 1])
                                lows.Add(currentPoint);
                        }
                        else
                        {
                            if (currentPoint < points[i - 1][j]
                                && currentPoint < points[i + 1][j]
                                && currentPoint < points[i][j - 1]
                                && currentPoint < points[i][j + 1])
                                lows.Add(currentPoint);
                        }
                    }
                }
            }

            Console.WriteLine("Part 1: " + (lows.Sum() + lows.Count()));
        }


        public static void Part2()
        {
            var points = new List<List<int>>();

            foreach (string line in System.IO.File.ReadLines(@"AppData\fulldata.txt"))
            {
                points.Add(line.ToCharArray().Select(x => Convert.ToInt32(x.ToString())).ToList());
            }

            var lows = new List<LowPoint>();

            for (int i = 0; i < points.Count(); i++)
            {
                for (int j = 0; j < points[i].Count(); j++)
                {
                    var currentPoint = points[i][j];
                    if (i == 0)
                    {
                        if (j == 0)
                        {
                            if (currentPoint < points[i + 1][j]
                                && currentPoint < points[i][j + 1])
                                lows.Add(new LowPoint(i, j));
                        }
                        else if (j == points[i].Count() - 1)
                        {
                            if (currentPoint < points[i + 1][j]
                                && currentPoint < points[i][j - 1])
                                lows.Add(new LowPoint(i, j));
                        }
                        else
                        {
                            if (currentPoint < points[i + 1][j]
                                && currentPoint < points[i][j - 1]
                                && currentPoint < points[i][j + 1])
                                lows.Add(new LowPoint(i, j));
                        }

                    }
                    else if (i == points.Count() - 1)
                    {
                        if (j == 0)
                        {
                            if (currentPoint < points[i - 1][j]
                                && currentPoint < points[i][j + 1])
                                lows.Add(new LowPoint(i, j));
                        }
                        else if (j == points[i].Count() - 1)
                        {
                            if (currentPoint < points[i - 1][j]
                                && currentPoint < points[i][j - 1])
                                lows.Add(new LowPoint(i, j));
                        }
                        else
                        {
                            if (currentPoint < points[i - 1][j]
                                && currentPoint < points[i][j - 1]
                                && currentPoint < points[i][j + 1])
                                lows.Add(new LowPoint(i, j));
                        }
                    }
                    else
                    {
                        if (j == 0)
                        {
                            if (currentPoint < points[i - 1][j]
                                && currentPoint < points[i + 1][j]
                                && currentPoint < points[i][j + 1])
                                lows.Add(new LowPoint(i, j));
                        }
                        else if (j == points[i].Count() - 1)
                        {
                            if (currentPoint < points[i - 1][j]
                                && currentPoint < points[i + 1][j]
                                && currentPoint < points[i][j - 1])
                                lows.Add(new LowPoint(i, j));
                        }
                        else
                        {
                            if (currentPoint < points[i - 1][j]
                                && currentPoint < points[i + 1][j]
                                && currentPoint < points[i][j - 1]
                                && currentPoint < points[i][j + 1])
                                lows.Add(new LowPoint(i, j));
                        }
                    }
                }
            }

            var basinCounts = new List<int>();

            var maxX = points.Count();
            var maxY = points[0].Count();

            var hitPoints = new List<LowPoint>();

            foreach(var low in lows)
            {
                basinCounts.Add(GetBasinForLow(points, low, maxX, maxY, hitPoints));
            }

            basinCounts.Sort();
            basinCounts.Reverse();

            var largest = basinCounts.Take(3);


            Console.WriteLine("Part 2: " + Multiply(largest.ToList()));
        }

        private static int Multiply(List<int> nums)
        {
            return nums[0] * nums[1] * nums[2];
        }


        private static int GetBasinForLow(List<List<int>> points, LowPoint low, int maxX, int maxY, List<LowPoint> hitPoints)
        {
            return GoSearch(points, low.x, low.y, maxX, maxY, Direction.UP, hitPoints);
        }

        private static int GoSearch(List<List<int>> points, int x, int y, int maxX, int maxY, Direction d, List<LowPoint> hitPoints)
        {
            var count = 0;
            var newX = x;
            var newY = y;

            if (hitPoints.Where(h => h.x == newX && h.y == newY).Count() > 0) return count;

            if (newY >= 0 && newY < maxY && newX >= 0 && newX < maxX)
            {
                if (points[newX][newY] < 9)
                {
                    count++;
                    hitPoints.Add(new LowPoint(newX, newY));
                }
                else return count;
            }
            else return count;

            if(newY > 0 && d != Direction.DOWN)
                count += GoSearch(points, newX, newY - 1, maxX, maxY, Direction.UP, hitPoints);

            if(newY < maxY && d != Direction.UP)
                count += GoSearch(points, newX, newY + 1, maxX, maxY, Direction.DOWN, hitPoints);

            if(newX > 0 && d != Direction.RIGHT)
                count += GoSearch(points, newX -1, newY, maxX, maxY, Direction.LEFT, hitPoints);

            if(newX < maxX && d != Direction.LEFT)
                count += GoSearch(points, newX + 1, newY, maxX, maxY, Direction.RIGHT, hitPoints);


            return count;
        }
        
    }

    //probably didn't need this after adding the hitpoints list
    public enum Direction
    {
        UP,
        DOWN,
        LEFT,
        RIGHT
    }

    public class LowPoint
    {
        public int x { get; set; }
        public int y { get; set; }
        public LowPoint(int x, int y)
        {
            this.x = x;
            this.y = y;
        }
    }
}


//Lots of crap that didn't work.

//public static void Part2()
//{
//    var points = new List<List<int>>();

//    foreach (string line in System.IO.File.ReadLines(@"AppData\testdata.txt"))
//    {
//        points.Add(line.ToCharArray().Select(x => Convert.ToInt32(x.ToString())).ToList());
//    }

//    var allBasins = new List<bool>();

//    for (int i = 0; i < points.Count(); i++)
//    {
//        for (int j = 0; j < points[i].Count(); j++)
//        {
//            var currentPoint = points[i][j];

//            if (currentPoint < 9)
//            {
//                allBasins.Add(true);
//            }
//            else if (currentPoint == 9)
//            {
//                allBasins.Add(false);
//            }
//        }
//    }

//    //hardcode lows count
//    var possibleBasins = new int[4];

//    var basinIndex = 0;
//    var iterator = 0;

//    for(int i = 0; i < allBasins.Count(); i++)
//    {
//        var basin = allBasins[i];

//        possibleBasins[basinIndex] += (basin) ? 1 : 0;

//        if (!basin && iterator != 0) basinIndex++;

//        iterator++;

//        if (iterator == 10)
//        {
//            iterator = 0;
//            basinIndex = 0;
//        }
//    }

//    Console.WriteLine("Part 2: " + (0));
//}


//public static void Part3()
//{
//    var points = new List<List<int>>();

//    foreach (string line in System.IO.File.ReadLines(@"AppData\testdata.txt"))
//    {
//        points.Add(line.ToCharArray().Select(x => Convert.ToInt32(x.ToString())).ToList());
//    }

//    var allBasins = new List<int>();
//    int iEnd = 0;
//    var jEnds = new int[points.Count()];

//    for (int i = 0; i < points.Count(); i++)
//    {
//        var iStart = (jEnds[i] < points.Count() - 1) ? 0: iEnd;
//        var (newCount, iEnding, jEndings) = FindBasin(iStart, jEnds, points);
//        iEnd = iEnding;
//        jEnds = jEndings;
//        allBasins.Add(newCount);
//    }

//    Console.WriteLine("Part 2: " + (0));
//}


//public static (int, int, int[]) FindBasin(int iStart, int[] jStarts, List<List<int>> points)
//{
//    var basinCount = 0;
//    var jEndings = new int[points.Count()];
//    int i;

//    for (i = iStart; i < points.Count(); i++)
//    {
//        var currentPoint = points[i][jStarts[i]];

//        if (currentPoint < 9)
//        {
//            var (newCount, jEnd) = FindBasinRow(jStarts[i], points[i]);
//            jEndings[i] = jEnd;
//            basinCount += newCount;
//        }
//        else if (currentPoint == 9)
//        {
//            return (basinCount, i, jEndings);
//        }
//    }

//    return (basinCount, i, jEndings);
//}

//public static (int, int) FindBasinRow(int jStart, List<int> col)
//{
//    var basinCount = 0;
//    int j;

//    for (j = jStart; j < col.Count(); j++)
//    {
//        var currentPoint = col[j];

//        if (currentPoint < 9)
//        {
//            basinCount++;
//        }
//        else if (currentPoint == 9)
//        {
//            return (basinCount, j);
//        }
//    }

//    return (basinCount, j);
//}