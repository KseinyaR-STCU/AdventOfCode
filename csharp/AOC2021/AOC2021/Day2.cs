namespace AOC2021
{
    using System;

    public static class Day2
    {

        public static void Part1()
        {
            var horizontal = 0;
            var vertical = 0;

            foreach (string line in System.IO.File.ReadLines(@"AppData\fulldata.txt"))
            {
                var courseValues = line.Split(' ');
                var direction = courseValues[0];
                var positionChange = Convert.ToInt32(courseValues[1]);
                if(direction == "forward")
                {
                    horizontal += positionChange;
                }
                else if(direction == "down")
                {
                    vertical += positionChange;
                }
                else
                {
                    vertical -= positionChange;
                }
            }

            Console.WriteLine("Part 1: " + horizontal * vertical);
        }

        public static void Part2()
        {
            var horizontal = 0;
            var vertical = 0;
            var aim = 0;

            foreach (string line in System.IO.File.ReadLines(@"AppData\fulldata.txt"))
            {
                var courseValues = line.Split(' ');
                var direction = courseValues[0];
                var positionChange = Convert.ToInt32(courseValues[1]);
                if (direction == "forward")
                {
                    horizontal += positionChange;
                    vertical += (aim * positionChange);
                }
                else if (direction == "down")
                {
                    aim += positionChange;
                }
                else
                {
                    aim -= positionChange;
                }
            }

            Console.WriteLine("Part 2: " + horizontal * vertical);
        }


    }
}
