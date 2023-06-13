package jetlag

type Hour struct {
	hour uint
}

func NewHour(hour uint) Hour {
	return Hour{hour}
}

func AddHours(hours ...Hour) Hour {
	var sum uint = 0
	for _, hour := range hours {
		sum += hour.hour
	}
	return NewHour(sum)
}

func (h Hour) LessThan(another Hour) bool {
	return h.hour < another.hour
}

func (h Hour) Till24() Hour {
	return NewHour(24 - h.hour)
}

type Record struct {
	departure Hour
	flight    Hour
	arrival   Hour
}

func NewRecord(departure, flight, arrival Hour) Record {
	return Record{departure, flight, arrival}
}

type Problem struct {
	records []Record
}

func NewProblem(records []Record) Problem {
	return Problem{records}
}

func (p Problem) Records() []Record {
	return p.records
}

type Answer struct {
	min Hour
	max Hour
}

func NewAnswer(min, max Hour) Answer {
	return Answer{min, max}
}

func Solve(p Problem) Answer {
	hours := []Hour{}
	for _, record := range p.Records() {
		hour := AddHours(record.departure, record.flight, record.arrival.Till24())
		hours = append(hours, hour)
	}
	return findMinMaxHour(hours)
}

func findMinMaxHour(hours []Hour) Answer {
	min := hours[0]
	max := hours[0]
	for _, hour := range hours {
		if hour.LessThan(min) {
			min = hour
		}
		if max.LessThan(hour) {
			max = hour
		}
	}
	return NewAnswer(min, max)
}
