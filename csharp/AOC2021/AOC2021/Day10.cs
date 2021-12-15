namespace AOC2021
{
    using System;
    using System.Collections;
    using System.Collections.Generic;
    using System.Linq;
    using System.Numerics;

    public static class Day10
    {

        public static void Part1()
        {
            var stack = new Stack<char>();

            var points = 0;

            foreach (string line in System.IO.File.ReadLines(@"AppData\testdata.txt"))
            {
                foreach(var character in line)
                {
                    if (IsOpen(character)) stack.Push(character);
                    else
                    {
                        var lastOpen = stack.Pop();
                        if (lastOpen == '(' && character == ')') continue;
                        else if (lastOpen == '{' && character == '}') continue;
                        else if (lastOpen == '[' && character == ']') continue;
                        else if (lastOpen == '<' && character == '>') continue;
                        else
                        {
                            if (character == ')') points += 3;
                            else if (character == ']') points += 57;
                            else if (character == '}') points += 1197;
                            else points += 25137;

                            break;
                        }
                    }
                }

                stack.Clear();
            }

            Console.WriteLine("Part 1: " + points);
        }

        public static void Part2()
        {
            var stack = new Stack();

            var incompletes = new List<Stack>();

            var isBroken = false;

            foreach (string line in System.IO.File.ReadLines(@"AppData\fulldata.txt"))
            {
                isBroken = false;
                foreach (var character in line)
                {
                    if (IsOpen(character)) stack.Push(character);
                    else
                    {
                        var lastOpen = (char)stack.Pop();
                        if (lastOpen == '(' && character == ')') continue;
                        else if (lastOpen == '{' && character == '}') continue;
                        else if (lastOpen == '[' && character == ']') continue;
                        else if (lastOpen == '<' && character == '>') continue;
                        else
                        {
                            isBroken = true;
                            break;
                        }
                    }
                }

                if (!isBroken) incompletes.Add((Stack)stack.Clone());

                stack.Clear();
            }

            var points = new List<BigInteger>();

            foreach(var thingy in incompletes)
            {
                var initialPoint = new BigInteger(0);

                while (thingy.Count != 0)
                {
                    initialPoint = initialPoint * 5;

                    var character = (char)thingy.Pop();

                    if (character == '(') initialPoint++;
                    else if (character == '[') initialPoint += 2;
                    else if (character == '{') initialPoint += 3;
                    else initialPoint += 4;
                }

                points.Add(initialPoint);
                
            }

            points.Sort();

            Console.WriteLine("Part 2: " + points.ElementAt(points.Count() /2));
        }


        public static bool IsOpen(char character)
        {
            var opens = new char[] { '[', '{', '(', '<' };
            return opens.Contains(character);
        }

        public static bool IsClosed(char character)
        {
            var closes = new char[] { ']', '}', ')', '>' };
            return closes.Contains(character);
        }
    }
}
