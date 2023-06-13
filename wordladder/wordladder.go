package wordladder

import "log"

type Word struct {
	word string
}

func NewWord(word string) Word {
	return Word{word}
}

func NewWords(words []string) []Word {
	results := []Word{}
	for _, w := range words {
		results = append(results, NewWord(w))
	}
	return results
}

func (w Word) LastChar() Char {
	return NewChar(string(w.word[len(w.word)-1]))
}

func (w Word) FirstChar() Char {
	return NewChar(string(w.word[0]))
}

type Problem struct {
	words []Word
}

func (p Problem) Words() []Word {
	return p.words
}

func NewProblem(words []Word) Problem {
	return Problem{words}
}

type Char struct {
	char string
}

func NewChar(char string) Char {
	if len(char) != 1 {
		log.Fatalf("illegal character: %s", char)
	}
	return Char{char}
}

type Answer struct {
	last  Char
	first Char
}

func NewAnswer(last, first Char) Answer {
	return Answer{last, first}
}

type Solver interface {
	Solve(p Problem) (bool, Answer)
}

func New() Solver {
	return &solverImpl{}
}

type solverImpl struct{}

func (s *solverImpl) Solve(p Problem) (bool, Answer) {
	words := p.Words()
	for i := 0; i < len(words)-1; i++ {
		word := words[i]
		nextWord := words[i+1]
		last := word.LastChar()
		first := nextWord.FirstChar()
		if last != first {
			return false, NewAnswer(last, first)
		}
	}
	return true, Answer{}
}
