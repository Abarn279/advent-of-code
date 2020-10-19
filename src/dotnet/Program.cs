using System;
using System.Collections.Generic;
using System.Collections;
using System.Linq;

namespace dotnet
{
    class Program
    {
        static void Main(string[] args)
        {
            // var floors = new List<HashSet<string>>()
            // {
            //     new HashSet<string>() { "HM", "LM" },
            //     new HashSet<string>() { "HG" },
            //     new HashSet<string>() { "LG" },
            //     new HashSet<string>(),
            // };

            var floors = new List<HashSet<string>>()
            {
                new HashSet<string>() { "TG", "TM", "PG", "SG", "EG", "EM", "DG", "DM" },
                new HashSet<string>() { "PM", "SM" },
                new HashSet<string>() { "XG", "XM", "RG", "RM" },
                new HashSet<string>()
            };

            var steps = Searches.Astar<(string, int)>(
                start: new AStarNode(floors, 0, 0),
                isGoalFunc: (AStarNode n) =>
                {
                    return n.Floors[0].Count == 0 && n.Floors[1].Count == 0 && n.Floors[2].Count == 0;
                },
                heuristicFunc: (AStarNode n) =>
                {
                    var total = 0;
                    for (var floorInd = 0; floorInd < 4; floorInd++) // Always 4 floors
                    {
                        total += (n.Floors[floorInd].Count * (3 - floorInd) / 2);
                    }
                    return total;
                },
                costFunc: (AStarNode a, AStarNode b) =>
                {
                    return 1;
                },
                getNeighborsFunc: (AStarNode n) =>
                {
                    var floors = n.Floors;
                    var elevator = n.Elevator;
                    var currentSteps = n.CurrentSteps;
                    var neighbors = new List<AStarNode>();

                    for (var i = 1; i < 3; i++)
                    {
                        if (floors[elevator].Count < i)
                            continue;

                        var combos = Combinations<string>(floors[elevator], i);

                        foreach (var d in new int[] { -1, 1 })
                        {
                            if (d == -1 && i == 2) continue;

                            foreach (IEnumerable combo in combos)
                            {
                                if (elevator + d < 0 || elevator + d > 3) continue;

                                var newFloors = floors.Select(s => new HashSet<string>(s.Select(v => v))).ToList();

                                foreach (string c in combo)
                                {
                                    newFloors[elevator].Remove(c);
                                    newFloors[elevator + d].Add(c);
                                }

                                if (!IsValid(newFloors))
                                    continue;

                                neighbors.Add(new AStarNode(newFloors, elevator + d, currentSteps + 1));
                            }
                        }
                    }

                    return neighbors;
                },
                getKeyFunc: (AStarNode n) =>
                {
                    var s = "";
                    foreach (var f in n.Floors)
                    {
                        var x = f.Select(x => x).OrderBy(x => x);
                        s += string.Join(",", x) + '|';
                    }
                    return (s, n.Elevator);
                }
            );

            Console.WriteLine(steps.Cost);
        }

        private static bool IsValid(List<HashSet<string>> floors)
        {
            foreach (var floor in floors)
            {
                var allGenerators = floor.Where(x => x[1] == 'G').ToList();
                var isRadioactive = allGenerators.Count > 0;

                foreach (var m in floor.Where(x => x[1] == 'M'))
                {
                    if (!floor.Contains(m[0] + "G") && isRadioactive) 
                        return false;
                }
            }
            
            return true;
        }

        private static IEnumerable Combinations<T>(IEnumerable<T> elements, int k)
        {
            var elem = elements.ToArray();
            var size = elem.Length;

            if (k > size) yield break;

            var numbers = new int[k];

            for (var i = 0; i < k; i++)
                numbers[i] = i;

            do
            {
                yield return numbers.Select(n => elem[n]);
            } while (NextCombination(numbers, size, k));
        }

        private static bool NextCombination(IList<int> num, int n, int k)
        {
            bool finished;

            var changed = finished = false;

            if (k <= 0) return false;

            for (var i = k - 1; !finished && !changed; i--)
            {
                if (num[i] < n - 1 - (k - 1) + i)
                {
                    num[i]++;

                    if (i < k - 1)
                        for (var j = i + 1; j < k; j++)
                            num[j] = num[j - 1] + 1;
                    changed = true;
                }
                finished = i == 0;
            }

            return changed;
        }
    }

    public class AStarNode : Priority_Queue.FastPriorityQueueNode
    {
        public AStarNode(List<HashSet<string>> floors, int elevator, int currentSteps)
        {
            Floors = floors;
            Elevator = elevator;
            CurrentSteps = currentSteps;
        }

        public List<HashSet<string>> Floors { get; set; }
        public int Elevator { get; set; }
        public int CurrentSteps { get; set; }
    }
}
