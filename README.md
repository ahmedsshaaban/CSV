# finddiff:
finddiff is a simple python tool to compare two CSV files and output the diferrent rows to a new CSV file in the same directory. it can compare files based on all header fields or based on specific header field(s).

## Instructions
<div class="highlight highlight-source-shell"><pre>.\finddiff.py file1 file2 "header_values"</pre></div>

 
- find rows that exist in file1 and don't exist in file2
- header_values : comma sperated values for the required Header fields or \all to use all header fields

<hr>

### Example1:

#### file1:
<div class="highlight highlight-source-shell"><pre>
Username,EmailAddress
user1,user1@example.com
user2,user2@example.com
user3,user3@example.com
user4,user4@example.com
</pre>
</div>


#### file2:
<div class="highlight highlight-source-shell"><pre>
Username,EmailAddress
user1,user1@example.com
user2,user2@example.com
user3,user3@example.com
</pre>
</div>

<div class="highlight highlight-source-shell"><pre>.\finddiff.py file1.csv file2.csv "Username"</pre></div>



#### output:
<div class="highlight highlight-source-shell"><pre>
Username,EmailAddress
user4,user4@example.com
</pre>
</div>

<hr>

### Example2:
#### file1:
<div class="highlight highlight-source-shell"><pre>
Username,EmailAddress
user1, user1@example.com
user2,user2@example.com
user3,user3@example.com
user4,different@example.com
</pre>
</div>

#### file2:
<div class="highlight highlight-source-shell"><pre>
Username,EmailAddress
user1, 
user2,user2@example.com
user3,
user4,user4@example.com
</pre>
</div>
<div class="highlight highlight-source-shell"><pre>.\finddiff.py file1.csv file2.csv "Username,EmailAddress"</pre></div>



#### output:
<div class="highlight highlight-source-shell"><pre>
Username,EmailAddress
user1, user1@example.com
user3,user3@example.com
user4,different@example.com
</pre>
</div>
<hr>

### Example3:

#### file1:
<div class="highlight highlight-source-shell"><pre>
Username,Database,EmailAddress
user1,DB-op,user1@example.com
user2,DB-mn,user2@example.com
user3,DB-kl,user3@example.com
user4,DB-ui,user4@example.com
</pre>
</div>

#### file2:
<div class="highlight highlight-source-shell"><pre>
Username,Database,EmailAddress
user1,DB-qw,user1@example.com
user2,DB-ty,user2@example.com
user3,DB-kj,user3@example.com
user4,DB-hg,user4@example.com
</pre>
</div>
<div class="highlight highlight-source-shell"><pre>.\finddiff.py file1.csv file2.csv "Username,EmailAddress"</pre></div>


in this case, matching is done using username and emailaddress , so output will be empty (no different rows)
however if we changed the values to:

<div class="highlight highlight-source-shell"><pre>
<ul>
<li>.\finddiff.py file1.csv file2.csv "Username,Database"</li>
<li>.\finddiff.py file1.csv file2.csv "Username,Datbase,EmailAddress"</li>
<li>.\finddiff.py file1.csv file2.csv \all </li>
</ul>
</pre></div>


#### output will be:
<div class="highlight highlight-source-shell"><pre>
Username,Database,EmailAddress
user1,DB-op,user1@example.com
user2,DB-mn,user2@example.com
user3,DB-kl,user3@example.com
user4,DB-ui,user4@example.com
</pre>
</div>
