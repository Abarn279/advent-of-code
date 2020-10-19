using System;
using System.Collections;
using System.Collections.Generic;
using Priority_Queue;

namespace dotnet
{
    public static partial class Searches
    {
        /// <summary>
        /// A* Algorithm
        /// </summary>
        /// <param name="start">The starting node</param>
        /// <param name="isGoalFunc">A function that defines whether or not the current node is the goal</param>
        /// <param name="heuristicFunc">A heauristic function</param>
        /// <param name="costFunc">A cost function between two neighbor nodes</param>
        /// <param name="getNeighborsFunc">A function that returns a set of all neighbors</param>
        /// <param name="getKeyFunc">A function that returns a key that represents a node, of type T</param>
        /// <typeparam name="T">The type for the keys of this graph</typeparam>
        /// <returns></returns>
        public static AStarResponse Astar<T>(AStarNode start,
                                Func<AStarNode, bool> isGoalFunc,
                                Func<AStarNode, double> heuristicFunc,
                                Func<AStarNode, AStarNode, double> costFunc,
                                Func<AStarNode, IList<AStarNode>> getNeighborsFunc,
                                Func<AStarNode, T> getKeyFunc)
        {
            var queue = new SimplePriorityQueue<AStarNode, double>();
            queue.Enqueue(start, 0);

            // A map of node key to it's previous connected node in the resulting path
            var lastNodeDict = new Dictionary<T, AStarNode>();
            // A map of node key to its cost from the starting node
            var costFromStart = new Dictionary<T, double>();

            // lastNodeDict[getKeyFunc(start)] = null;
            costFromStart[getKeyFunc(start)] = 0;

            var found = false;
            AStarNode current = null;
            AStarNode final = null;
            while (queue.Count > 0)
            {
                current = queue.Dequeue();

                if (isGoalFunc(current))
                {
                    found = true;
                    final = current;
                    break;
                }

                foreach (var neighbor in getNeighborsFunc(current))
                {
                    var newCost = costFromStart[getKeyFunc(current)] + costFunc(current, neighbor);

                    if (!costFromStart.ContainsKey(getKeyFunc(neighbor)) || newCost < costFromStart[getKeyFunc(neighbor)])
                    {
                        costFromStart[getKeyFunc(neighbor)] = newCost;
                        var priority = newCost + heuristicFunc(neighbor);
                        queue.Enqueue(neighbor, priority);
                        lastNodeDict[getKeyFunc(neighbor)] = current;
                    }
                }
            }

            if (found)
            {
                // // Start with final , work backward
                // var path = new NavigationNodePath(final);
                // // var previous = new NavigationNodePath(lastNodeDict[]);

                // var previousNodeExists = lastNodeDict.TryGetValue(getKeyFunc(path.Node), out var previousNode);
                // while (previousNodeExists)
                // {
                //     var previous = new NavigationNodePath(previousNode);
                //     path.Previous = previous;
                //     path.Previous.Next = path;

                //     path = path.Previous;

                //     if (path.Node == null) break;
                //     previousNodeExists = lastNodeDict.TryGetValue(getKeyFunc(path.Node), out previousNode);
                // }

                return new AStarResponse { Cost = costFromStart[getKeyFunc(current)] };
            }

            return null;
        }
    }

    public class AStarResponse
    {
        public double Cost { get; set; }
    }
}