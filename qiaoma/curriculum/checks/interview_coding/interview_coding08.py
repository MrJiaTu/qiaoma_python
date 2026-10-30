assert simplify_path("/a/./b/../../c/") == "/c"
assert simplify_path("/../") == "/"
assert simplify_path("/home//foo/") == "/home/foo"
