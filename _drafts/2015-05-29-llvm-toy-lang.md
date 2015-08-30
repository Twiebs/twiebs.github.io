layout: post
---
title: Writing a toy language with LLVM
tags:
      - C++
      - LLVM
      - Compiler
---

##Resources
If you are also interested in building your own toy language these resources may be helpful:
[LLVM Tutorial Page](http://llvm.org/docs/tutorial/)
While i was writing this post i just discovered this at the footnote of this page

I started off following the tutorial for the Kaleidoscope Language on the LLVM tutorial page.
The tutorial was written when LLVM was in 2.x something but LLVM is now at v3.6 at the time of this post
When running functions via JIT in Kaledioscope the following code snipit will no longer work.

{% highlight cpp %}
if (Function *LF = F->Codegen()) {
  // JIT the function, returning a function pointer.
  void *FPtr = JITHelper->getPointerToFunction(LF);

  // Cast it to the right type (takes no arguments, returns a double) so we
  // can call it as a native function.
  double (*FP)() = (double (*)())(intptr_t)FPtr;
  fprintf(stderr, "Evaluated to %f\n", FP());
}
{% endhighlight %}

Using this code here is a sample Kaledioscope program and how the ExecutionEngine will evaluate it

{% highlight python %}
def foo(x) x;
foo(4); #returns 4
foo(5); #still returns 4
foo(32349546234); #still returns 4
{% endhighlight %}

ExecutionEngine::getPointerToFunction(Function*) has been deprecated in the current version of LLVM

To correct this problem with Kaleidoscope ExecutionEngine::runFunction(std::string name) is used to run a function directly

Writing a toy language can be a lot of fun.  I teaches you about how compilers work and ultimatly makes you a better programmer.

LLVM is a compiler framework that handles codegen.  
JIT
