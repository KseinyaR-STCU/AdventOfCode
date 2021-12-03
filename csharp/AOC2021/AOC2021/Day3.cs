namespace AOC2021
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    public static class Day3
    {

        public static void Part1()
        {
            var size = 12;
            var bitCounts = new int[size];

            var totalCount = 0;

            foreach (string line in System.IO.File.ReadLines(@"AppData\fulldata.txt"))
            {
                for(int i = 0; i < size; i++)
                {
                    if (line[i] == '1') bitCounts[i]++;
                }

                totalCount++;
            }

            var halfCount = totalCount / 2;
            var gamma = "";
            var epsilon = "";

            for (int i = 0; i < size; i++)
            {
                gamma += (bitCounts[i] >= halfCount) ? "1" : "0";
                epsilon += (bitCounts[i] < halfCount) ? "1" : "0";

            }

            Console.WriteLine("Part 1: " + Convert.ToInt32(gamma, 2) * Convert.ToInt32(epsilon, 2));
        }

        public static void Part2()
        {
            var size = 12;

            var allNumbers = new List<string>();

            foreach (string line in System.IO.File.ReadLines(@"AppData\fulldata.txt"))
            {
                allNumbers.Add(line);
            }

            var totalCount = allNumbers.Count();

            var bitCountOx = 0;
            var subListOx = allNumbers;
            var checkBitOx = '1';
            var ox = -1;

            var bitCountCo = 0;
            var subListCo = allNumbers;
            var checkBitCo = '0';
            var co = -1;

            for(int i = 0; i < size; i++)
            {
                if(ox == -1)
                {
                    totalCount = subListOx.Count();
                    bitCountOx = subListOx.Count(x => x[i] == '1');

                    checkBitOx = (totalCount - bitCountOx <= bitCountOx) ? '1' : '0';

                    subListOx = subListOx.Where(x => x[i] == checkBitOx).ToList();
                    if (subListOx.Count() == 1) ox = Convert.ToInt32(subListOx.First(), 2);
                }
                
                if(co == -1)
                {
                    totalCount = subListCo.Count();
                    bitCountCo = subListCo.Count(x => x[i] == '1');

                    checkBitCo = (totalCount - bitCountCo > bitCountCo) ? '1' : '0';

                    subListCo = subListCo.Where(x => x[i] == checkBitCo).ToList();
                    if (subListCo.Count() == 1) co = Convert.ToInt32(subListCo.First(), 2);
                }
            }

            Console.WriteLine("Part 2: " + ox * co);
        }
    }
}
