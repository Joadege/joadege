using System;
using System.Collections;
using System.Collections.Generic;
using System.Runtime.InteropServices.WindowsRuntime;
using UnityEngine;

public class demo2 : MonoBehaviour
{ 
    // Start is called before the first frame update
    public string myname = "Player";
     

    

//return result


   void Start()
{
    // Array of integers
    int[] myNum = { 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 };

    // Array of team names
    string[] Teams = { "Fla", "UGA", "KY", "Miz", "SC", "Ten", "Van", "Ala", "Ark", "Aub", "LSU", "Mis", "OLM", "TAM" };

    // Display player name
    Debug.Log(myName);

    // Display the first team name
    Debug.Log(Teams[0]);

    // Iterate through Teams array using a loop
    Debug.Log("Team List:");
    foreach (string team in Teams)
    {
        Debug.Log(team);
    }

    // Call the Add method and display the result
    void Start()
{
    int result = Add(8, 8); // Call the Add method with arguments 8 and 8
    Debug.Log("Result of addition: " + result); // Log the result
}

// Define the Add method to return the sum of two integers
int Add(int a, int b)
{
    return a + b; // Return the sum
}

    }

    

    // Update is called once per frame
    
}