# Go语言中的异常处理机制.

  在Go语言中，panic是一个运行时错误（很像其他语言中的异常，因此本书将panic直接翻译为“异常”）。我们可以使用内置的panic()函数来触发一个异常，还可以使用recover()函数（参见5.5节）来在其调用栈上阻止该异常的传播。理论上，Go语言的panic/recover功能可以用于多用途的错误处理机制，但我们并不推荐这么用。  
  
  