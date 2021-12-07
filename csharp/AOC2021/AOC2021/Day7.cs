namespace AOC2021
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    public static class Day7
    {
        public static void Part1()
        {
            var crabs = new List<int>();

            foreach (string line in System.IO.File.ReadLines(@"AppData\fulldata.txt"))
            {
                crabs.AddRange(line.Split(',').Select(x => Convert.ToInt32(x)).ToList());
            }

            crabs.Sort();

            var median = (crabs.Count() % 2 == 0) ? crabs[crabs.Count()/2] : crabs[crabs.Count()/2+1];

            var fuel = 0;

            foreach(var crab in crabs)
            {
                fuel += (crab > median) ? (crab - median) : (median - crab);
            }

            Console.WriteLine("Part 1: " + fuel);
        }

        public static void Part2()
        {
            var crabs = new List<int>();

            foreach (string line in System.IO.File.ReadLines(@"AppData\fulldata.txt"))
            {
                crabs.AddRange(line.Split(',').Select(x => Convert.ToInt32(x)).ToList());
            }

            crabs.Sort();

            //I can't believe this worked LMAO
            var mean = (int) crabs.Average();
            var meanPlus1 = mean + 1;
            var meanMinus1 = mean - 1;

            var fuel = 0;
            var fuelPlus1 = 0;
            var fuelMinus1 = 0;

            foreach (var crab in crabs)
            {
                fuel += (crab > mean) ? getCost(crab - mean) : getCost(mean - crab);
                fuelPlus1 += (crab > meanPlus1) ? getCost(crab - meanPlus1) : getCost(meanPlus1 - crab);
                fuelMinus1 += (crab > meanMinus1) ? getCost(crab - meanMinus1) : getCost(meanMinus1 - crab);
            }

            Console.WriteLine("Part 2: " + Math.Min( Math.Min(fuel, fuelPlus1), fuelMinus1));
        }

        private static int getCost(int steps)
        {
            var total = 0;
            for(int i = 1; i <= steps; i++)
            {
                total += i;
            }

            return total;
        }

    }
}
