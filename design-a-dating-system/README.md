<h2>  Design a Dating System</h2><hr><div><p>Design a simple dating system like Tinder with the following features:</p>

<ol>
	<li>Register a user with their gender, age, preferences, and interests.</li>
	<li>Find <strong>matching</strong> users according to their preferred gender, preferred age range, and common interests.</li>
</ol>

<p>Implement the <code>Tinder</code> class:</p>

<ul>
	<li><code>Tinder()</code> Initializes the object.</li>
	<li><code>void signup(int userId, int gender, int preferredGender, int age, int minPreferredAge, int maxPreferredAge, List&lt;String&gt; interests)</code> Registers a user with the given attributes.</li>
	<li><code>List&lt;Integer&gt; getMatches(int userId)</code> Returns the top <code>5</code> matches for the given user. The returned matches should satisfy the following:
	<ul>
		<li>The returned user's gender should <strong>equal</strong> the given user's <code>preferredGender</code>.</li>
		<li>The returned user's age should be <strong>between</strong> the given user's <code>minPreferredAge</code> and <code>maxPreferredAge</code> (inclusive).</li>
		<li>There should be <strong>at least</strong> <code>1</code> common interest between the returned user and the given user.</li>
		<li>The results should be sorted in <strong>decreasing</strong> order by the number of common interests. If there is a tie, it should be sorted in <strong>increasing</strong> order by <code>userId</code>.</li>
		<li>If there are fewer than <code>5</code> matches, return as many as possible.</li>
		<li>Note that the given user might not necessarily be a match for the returned users.</li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input</strong>
["Tinder", "getMatches", "signup", "getMatches", "signup", "getMatches", "getMatches", "signup", "signup", "getMatches", "signup", "getMatches", "getMatches", "signup", "getMatches", "getMatches"]
[[], [1], [1, 0, 1, 25, 20, 30, ["Singing", "Dancing", "Reading", "Skating"]], [1], [2, 1, 0, 27, 23, 30, ["Painting", "Basketball"]], [1], [2], [3, 1, 0, 25, 20, 30, ["Singing", "Skating"]], [4, 1, 0, 25, 20, 30, ["Singing", "Writing", "Coding"]], [1], [5, 1, 0, 31, 24, 37, ["Singing", "Dancing", "Reading", "Skating"]], [1], [5], [6, 0, 1, 30, 25, 33, ["Volleyball", "Skating"]], [5], [6]]
<strong>Output</strong>
[null, [], null, [], null, [], [], null, null, [3, 4], null, [3, 4], [1], null, [1, 6], [3, 5]]

<strong>Explanation</strong>
Tinder tinder = new Tinder();
tinder.getMatches(1); // return [], there is no user with userId 1.
tinder.signup(1, 0, 1, 25, 20, 30, ["Singing", "Dancing", "Reading", "Skating"]);
tinder.getMatches(1); // return [], no users besides user 1 have signed up yet.
tinder.signup(2, 1, 0, 27, 23, 30, ["Painting", "Basketball"]);
tinder.getMatches(1); // return [], user 2 has no common interests with user 1, so there are no matches.
tinder.getMatches(2); // return [], similarly, user 1 has no common interests with user 2.
tinder.signup(3, 1, 0, 25, 20, 30, ["Singing", "Skating"]);
tinder.signup(4, 1, 0, 25, 20, 30, ["Singing", "Writing", "Coding"]);
tinder.getMatches(1); // return [3, 4], both users 3 and 4 are in the age range for user 1 and
                      // are the preferred gender of user 1. Since user 3 has 2 common interests
                      // and user 4 has 1 common interest, user 3 is returned before user 4.
tinder.signup(5, 1, 0, 31, 24, 37, ["Singing", "Dancing", "Reading", "Skating"]);
tinder.getMatches(1); // return [3, 4], user 5 has an age larger than the maxPreferredAge of user 1.
tinder.getMatches(5); // return [1], user 1 has the preferred age, gender, and has 4 common interests.
tinder.signup(6, 0, 1, 30, 25, 33, ["Volleyball", "Skating"]);
tinder.getMatches(5); // return [1, 6], user 6 has the preferred age, gender, and has 1 common interest.
tinder.getMatches(6); // return [3, 5], users 3 and 5 both have the preferred age, gender,
                      // and have 1 common interest. Since they both have 1 common interest
                      // and 3 &lt; 5, user 3 is returned before user 5.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= userId &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= gender, preferredGender &lt;= 1</code></li>
	<li><code>18 &lt;= age &lt;= 90</code></li>
	<li><code>18 &lt;= minPreferredAge &lt;= maxPreferredAge &lt;= 90</code></li>
	<li><code>1 &lt;= interests.length &lt;= 5</code></li>
	<li><code>1 &lt;= interests[i].length &lt;= 20</code></li>
	<li><code>interests[i]</code> consists of lowercase and uppercase English letters and <code>' '</code>.</li>
	<li>All strings in <code>interests</code> are unique.</li>
	<li>At most <code>1000</code> calls will be made to <code>signup</code> and <code>getMatches</code>.</li>
	<li><code>userId</code> will be <strong>unique</strong> across all calls made to <code>signup</code>.</li>
</ul>
</div>