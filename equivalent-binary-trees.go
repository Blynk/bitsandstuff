package main

import (
	"golang.org/x/tour/tree"
	"fmt"
)

type valueCount map[int]int

// Walk walks the tree t sending all values
// from the tree to the channel ch.
func Walk(t *tree.Tree, ch chan int) {
	defer close(ch)
	if t == nil {
		return
	}

	queue := []*tree.Tree{t}
	
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		ch <- node.Value
		if node.Left != nil {
			queue = append(queue, node.Left)
		}
		if node.Right != nil {
			queue = append(queue, node.Right)
		}
	}
}

// Same determines whether the trees
// t1 and t2 contain the same values.
func Same(t1, t2 *tree.Tree) bool {
	c1 := make(chan int)
	c2 := make(chan int)
	
	go Walk(t1, c1)
	go Walk(t2, c2)
	
	count1, count2 := collectValues(c1, c2)
	
	return CompareCounters(count1, count2)
}

func collectValues(c1, c2 chan int) (valueCount, valueCount) {
	count1, count2 := make(valueCount), make(valueCount)
	for c1 != nil || c2 != nil {
		select {
		case val, ok := <- c1:
			if !ok {
				c1 = nil
				continue
			}
			count1[val]++
		case val, ok := <- c2:
			if !ok {
				c2 = nil
				continue
			}
			count2[val]++
		}
	}
	return count1, count2
}

func CompareCounters(c1, c2 map[int]int) bool {
	defer func() {
		fmt.Println(c1)
		fmt.Println(c2)
	}()

	if c1 == nil && c2 == nil {
		return true
	}
	
	if c1 == nil || c2 == nil || len(c1) != len(c2) {
		fmt.Println("maps not the same length")
		return false
	}
	
	for k, v1 := range c1 {
		v2, exists := c2[k]
		if !exists {
			fmt.Println("missing key:", k)
			return false
		} else if v1 != v2 {
			fmt.Println("found mismatch: ", v1, " != ", v2)
			return false
		}
	}
	
	return true
}

func main() {
	fmt.Println(Same(tree.New(1), tree.New(1)))
	fmt.Println(Same(tree.New(1), tree.New(2)))
}
