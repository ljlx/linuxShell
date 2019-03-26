package main

func infiniteFor() {
	index := 1
	for {
		if index == 10 {
			break
		}
		index++
		println(index)
	}
}

func main() {
	infiniteFor()
}
