namespace AOC2021
{
    using System;

    public static class Day1
    {

        public static void Part1()
        {
            var previousMeasurement = -1;
            var increaseCount = 0;

            foreach (string line in System.IO.File.ReadLines(@"AppData\fulldata.txt"))
            {
                var newMeasurement = Convert.ToInt32(line);
                if(newMeasurement > previousMeasurement && previousMeasurement != -1) increaseCount++;

                previousMeasurement = newMeasurement;
            }

            Console.WriteLine("Part 1: " + increaseCount);
        }

        public static void Part2()
        {
            int measurement1 = -1, measurement2 = -1, measurement3 = -1;
            var firstWindow = -1;
            var secondWindow = -1;
            var increaseCount = 0;

            foreach (string line in System.IO.File.ReadLines(@"AppData\fulldata.txt"))
            {
                var newMeasurement = Convert.ToInt32(line);

                //Initializing first three
                if (measurement1 == -1) measurement1 = newMeasurement;
                else if (measurement2 == -1) measurement2 = newMeasurement;
                else if (measurement3 == -1)
                {
                    measurement3 = newMeasurement;
                    firstWindow = measurement1 + measurement2 + measurement3;
                }
                else
                {
                    secondWindow = firstWindow - measurement1 + newMeasurement;
                    if (secondWindow > firstWindow) increaseCount++;

                    measurement1 = measurement2;
                    measurement2 = measurement3;
                    measurement3 = newMeasurement;
                    firstWindow = secondWindow;
                }
            }

            Console.WriteLine("Part 2: " + increaseCount);
        }


    }
}
