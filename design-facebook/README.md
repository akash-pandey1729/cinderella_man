<h2>  Design Facebook</h2><hr><div><p>Design a system like <strong>Facebook</strong> with the following features:</p>

<ol>
	<li>A user can write a <strong>post</strong>.</li>
	<li>Two users can become <strong>friends</strong> with each other.</li>
	<li>Users can see all the posts written by their friends.</li>
</ol>

<p>Implement the <code>Facebook</code> class:</p>

<ul>
	<li><code>Facebook()</code> Initializes the object.</li>
	<li><code>void writePost(int userId, String postContent)</code> The user with id <code>userId</code> writes a post with the content <code>postContent</code>.</li>
	<li><code>void addFriend(int user1, int user2)</code> <code>user1</code> and <code>user2</code> become friends with each other. This call should be <strong>ignored</strong> if <code>user1</code> and <code>user2</code> are already friends.</li>
	<li><code>List&lt;String&gt; showPosts(int userId)</code> Returns all the posts made by the friends of the user with id <code>userId</code> ordered by the <strong>latest</strong> ones first, including ones made before they became friends. <strong>Note</strong> that the posts made by user <code>userId</code> should <strong>not</strong> be returned.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input</strong>
["Facebook", "addFriend", "writePost", "writePost", "writePost", "writePost", "showPosts", "showPosts", "addFriend", "showPosts", "showPosts", "showPosts"]
[[], [1, 2], [1, "postone"], [2, "posttwo"], [3, "postthree"], [2, "postfour"], [2], [3], [2, 3], [1], [2], [3]]
<strong>Output</strong>
[null, null, null, null, null, null, ["postone"], [], null, ["postfour", "posttwo"], ["postthree", "postone"], ["postfour", "posttwo"]]

<strong>Explanation</strong>
Facebook facebook = new Facebook();
facebook.addFriend(1, 2); // Users 1 and 2 become friends.
facebook.writePost(1, "postone"); // "postone" is posted by user 1.
facebook.writePost(2, "posttwo"); // "posttwo" is posted by user 2.
facebook.writePost(3, "postthree"); // "postthree" is posted by user 3.
facebook.writePost(2, "postfour"); // "postfour" is posted by user 2.
facebook.showPosts(2); // return ["postone"]
                       // User 2 has only one friend, which is user 1 who has posted one time so far.
facebook.showPosts(3); // return []
                       // User 3 does not have any friends yet, so we return [].
facebook.addFriend(2, 3); // Users 2 and 3 become friends.
facebook.showPosts(1); // return ["postfour", "posttwo"]
                       // The only friend of user 1 is user 2 who has two posts, so we return them.
facebook.showPosts(2); // return ["postthree", "postone"]
                       // Users 1 and 3 are the friends of user 2.
                       // Both users 1 and 3 have one post each, but user 3 posted last,
                       // so we return user 3's post first.
facebook.showPosts(3); // return ["postfour", "posttwo"]
                       // The only friend of user 3 is user 2 who has two posts.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= userId &lt;= 1000</code></li>
	<li><code>1 &lt;= postContent.length &lt;= 100</code></li>
	<li><code>user1 != user2</code></li>
	<li><code>postContent</code> consists of lowercase English letters.</li>
	<li>At most <code>100</code> calls will be made to <code>writePost</code>.</li>
	<li>At most <code>1000</code> calls will be made to <code>addFriend</code>.</li>
	<li>At most <code>100</code> calls will be made to <code>showPosts</code>.</li>
</ul>
</div>