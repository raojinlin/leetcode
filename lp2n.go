package main

import (
	"bufio"
	"flag"
	"fmt"
	"os"
	"regexp"
	"strings"
)

func upperFirst(token string) string {
	if token == "" {
		return ""
	}

	t := strings.ToLower(token)
	t = strings.ToUpper(string(t[0])) + token[1:]

	return t
}

func toTokens(title string) []string {
	reg, _ := regexp.Compile("\\s|-|_|\\.")
	return reg.Split(title, 10)
}

// leetcode problem name to file name
//
// input:
// title = "1588. Sum of All Odd Length Subarrays"
// prefix = "P"
// suffix = ".py"
//
// output:
// P1588_SumOfAllOddLengthSubarrays.py
func convertProblemTitle(title, prefix, suffix string) string {
	tokens := toTokens(title)
	filename := prefix + strings.Replace(tokens[0], ".", "", 1) + "_"

	for _, token := range tokens[1:] {
		filename += upperFirst(token)
	}

	return filename + suffix
}

func main() {
	var title string
	var prefix string
	var suffix string
	var stdin bool

	flag.BoolVar(&stdin, "stdin", true, "read problem name from the standard input")
	flag.StringVar(&title, "title", "", "problem name, include problem number, required")
	flag.StringVar(&prefix, "prefix", "P", "problem number prefix")
	flag.StringVar(&suffix, "suffix", ".py", "filename suffix")

	flag.Parse()

	if title == "" && stdin {
		reader := bufio.NewReader(os.Stdin)
		title, _ = reader.ReadString('\n')
		title = strings.Replace(title, "\n", "", 1)
	}

	if title == "" {
		fmt.Println("convert leetcode problem name to filename")
		flag.Usage()
		return
	}

	fmt.Println(convertProblemTitle(title, prefix, suffix))
}
