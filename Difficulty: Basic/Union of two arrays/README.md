<h2><a href="https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1">Union of two arrays</a></h2><h3>Difficulty Level : Difficulty: Basic</h3><hr><div class="problems_problem_content__Xm_eO" style="null;"><p style="null;"><span style="font-size: 18px;;">Given two arrays <strong style="null;">a[]</strong>&nbsp;and <strong style="null;">b[]</strong>&nbsp;of size <strong style="null;">n</strong>&nbsp;and <strong style="null;">m</strong> respectively. The task is to find the number of elements in the union between these two arrays. </span></p>
<p style="null;"><span style="font-size: 18px;;">Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in the union.</span></p>
<p style="null;"><strong style="null;"><span style="font-size: 18px;;">Note : </span></strong><span style="font-size: 18px;;">Elements are not necessarily distinct.</span></p>
<p style="null;"><span style="font-size: 18px;;"><strong style="null;">Example 1:</strong></span></p>
<pre style="null;"><span style="font-size: 18px;;"><strong style="null;">Input:
</strong>5 3
1 2 3 4 5
1 2 3
<strong style="null;">Output: 
</strong>5<strong style="null;">
Explanation: 
</strong>1, 2, 3, 4 and 5 are the
elements which comes in the union set
of both arrays. So count is 5.</span>
</pre>
<p style="null;"><span style="font-size: 18px;;"><strong style="null;">Example 2:</strong></span></p>
<pre style="null;"><span style="font-size: 18px;;"><strong style="null;">Input:
</strong>6 2 
85 25 1 32 54 6
85 2 
<strong style="null;">Output: 
</strong>7<strong style="null;">
Explanation: 
</strong>85, 25, 1, 32, 54, 6, and
2 are the elements which comes in the
union set of both arrays. So count is 7.</span></pre>
<p style="null;"><strong style="null;"><span style="font-size: 18px;;">Your Task:</span></strong><br style="null;"><span style="font-size: 18px;;">Complete <strong style="null;">doUnion </strong>function that takes<strong style="null;"> a, n, b, m as parameters and returns</strong> the count of union elements of the&nbsp;two arrays. The <strong style="null;">printing </strong>is done by the <strong style="null;">driver </strong>code.</span></p>
<p style="null;"><span style="font-size: 18px;;"><strong style="null;">Constraints:</strong></span><br style="null;"><span style="font-size: 18px;;">1 ≤ n, m&nbsp;≤ 10<sup style="null;">5</sup><br style="null;">0 ≤ a[i], b[i] &lt;&nbsp;10<sup style="null;">5</sup></span></p>
<p style="null;"><span style="font-size: 18px;;"><strong style="null;">Expected Time Complexity </strong>: O(n+m)<br style="null;"><strong style="null;">Expected Auxilliary Space</strong> : O(n+m)</span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Zoho</code>&nbsp;<code>Rockstand</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Hash</code>&nbsp;<code>Mathematical</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;