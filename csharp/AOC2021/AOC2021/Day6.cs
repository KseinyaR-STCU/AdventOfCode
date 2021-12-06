namespace AOC2021
{
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Numerics;

    public static class Day6
    {
        public static void Part1()
        {
            var startFish = new List<int>();

            foreach (string line in System.IO.File.ReadLines(@"AppData\testdata.txt"))
            {
                startFish.AddRange(line.Split(',').Select(x => Convert.ToInt32(x)).ToList());
            }

            var newFish = 0;

            for(int i = 0; i < 80; i++)
            {
                for (int j = 0; j < startFish.Count(); j++)
                {
                    if (startFish[j] == 0)
                    {
                        newFish++;
                        startFish[j] = 6;
                    }
                    else
                    {
                        startFish[j]--;
                    }
                }

                for (int j = 0; j < newFish; j++)
                {
                    startFish.Add(8);
                }
                newFish = 0;
            }

            Console.WriteLine("Part 1: " + startFish.Count());
        }

        //WOOOOOWWWWW
        public static void Part2()
        {
            var fishesCount = new List<BigInteger> {0,0,0,0,0,0,0,0,0 };
            var totalDays = 256;

            foreach (string line in System.IO.File.ReadLines(@"AppData\fulldata.txt"))
            {
                var start = line.Split(',').Select(x => Convert.ToInt32(x)).ToList();

                foreach(var number in start)
                {
                    fishesCount[number]++;
                }
            }

            for(int i = 0; i < totalDays; i++)
            {
                var temp = fishesCount[0];

                fishesCount.RemoveAt(0);
                fishesCount.Add(temp);
                fishesCount[6] += temp;
            }

            Console.WriteLine("Part 2: " + Sum(fishesCount));
        }

        private static BigInteger Sum(List<BigInteger> counts)
        {
            BigInteger totalSum = 0;
            for (int i = 0; i < counts.Count(); i++)
            {
                totalSum += counts[i];
            }
            return totalSum;
        }
    }
}
