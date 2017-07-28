class BlogEntry {
//name, blogText
	constructor(name, blogText){
		this.name = name;
		this.blogText = blogText;
	}
}

function addEntryToBlog() {
  //Create new blog entry
  var name = document.getElementById("blogEntryName").value
  var blog = document.getElementById("blogEntryText").value
  var blogEntry = new BlogEntry(name, blog);
  //Add the new entry, name and date to the blog
  createBlogEntryElement(blogEntry);
  createFooterElement(blogEntry);

  document.getElementById("blogEntryName").innerHTML = "";
  document.getElementById("blogEntryText").innerHTML = "";

}

function createBlogEntryElement(blogEntry) {
	var blog_text = blogEntry.blogText;
	var node = document.createElement("div");
	node.className = "blogEntry";
	var blogDetails = document.getElementById("blogDetails");
	node.innerText = blog_text;
	blogDetails.appendChild(node);

}

function createFooterElement(blogEntry) {
	var blog_name = blogEntry.name;
	var node2 = document.createElement("div");
	node2.className = "blogDate";
	var x = Date();
	node2.innerText = "- " + blog_name + " " + x;
	blogDetails.appendChild(node2);
}
