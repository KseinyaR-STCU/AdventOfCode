namespace AOC2021
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    public static class Day8
    {
        public static void Part1()
        {
            var outputs = new List<int>();

            foreach (string line in System.IO.File.ReadLines(@"AppData\fulldata.txt"))
            {
                outputs.AddRange(line.Split('|')[1].Split(' ').Select(x => Convert.ToInt32(x.Trim().Length)).ToList());
            }

            var ones = outputs.Count(x => x == 2);
            var fours = outputs.Count(x => x == 4);
            var sevens = outputs.Count(x => x == 3);
            var eights = outputs.Count(x => x == 7);

            Console.WriteLine("Part 1: " + (ones + fours + sevens + eights));
        }

        public static void Part2()
        {
            var totalCount = 0;

            foreach (string line in System.IO.File.ReadLines(@"AppData\fulldata.txt"))
            {
                var splitLine = line.Split('|');
                var signals = splitLine[0].Split(' ').Select(x => x.Trim()).ToList();
                var outputs = splitLine[1].Split(' ').Select(x => x.Trim()).ToList();

                //obvious ones
                var realOne = signals.First(x => x.Length == 2);
                var realFour = signals.First(x => x.Length == 4);
                var realSeven = signals.First(x => x.Length == 3);
                var realEight = signals.First(x => x.Length == 7);

                //0, 6, and 9 all have 6 characters
                var length6 = signals.Where(x => x.Length == 6).ToList();

                var realNine = length6.First(x => isNine(realFour, x));
                length6.Remove(realNine);
                var realZero = length6.First(x => isZero(realOne, x));
                length6.Remove(realZero);
                var realSix = length6.First();

                //Thanks 9
                var bottomLeft = realEight.Where(x => !realNine.Contains(x)).First();

                //Thanks 6
                var topRight = realEight.Where(x => !realSix.Contains(x)).First();

                //2, 3, and 5 all have 5 characters
                var length5 = signals.Where(x => x.Length == 5).ToList();

                var realTwo = length5.First(x => x.Contains(bottomLeft));
                length5.Remove(realTwo);
                var realThree = length5.First(x => x.Contains(topRight));
                length5.Remove(realThree);
                var realFive = length5.First();

                var number = "";
                foreach (var output in outputs.Where(x => !String.IsNullOrWhiteSpace(x)))
                {
                    if (containsAllChars(output, realZero)) number += "0";
                    else if (containsAllChars(output,realOne)) number += "1";
                    else if (containsAllChars(output,realTwo)) number += "2";
                    else if (containsAllChars(output, realThree)) number += "3";
                    else if (containsAllChars(output, realFour)) number += "4";
                    else if (containsAllChars(output, realFive)) number += "5";
                    else if (containsAllChars(output, realSix)) number += "6";
                    else if (containsAllChars(output, realSeven)) number += "7";
                    else if (containsAllChars(output, realNine)) number += "9";
                    else if (containsAllChars(output, realEight)) number += "8";
                }

                var actualOutput = Convert.ToInt32(number);

                totalCount += actualOutput;

            }
            Console.WriteLine("Part 2: " + (totalCount));
        }

        //ew
        private static bool isNine(string four, string possibleNine)
        {
            return (possibleNine.Contains(four[0])
                && possibleNine.Contains(four[1])
                && possibleNine.Contains(four[2])
                && possibleNine.Contains(four[3]));
        }

        private static bool isZero(string one, string possibleZero)
        {
            return (possibleZero.Contains(one[0])
                && possibleZero.Contains(one[1]));
        }

        private static bool containsAllChars(string output, string number)
        {
            return output.Length == number.Length && output.All(x => number.Contains(x));
        }
    }
}
