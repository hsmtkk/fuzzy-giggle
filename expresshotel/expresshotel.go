package expresshotel

type Internship struct {
	Begin int
	End   int
}

type Problem struct {
	ExpressFee     int
	HotelFee       int
	InternshipDays []Internship
}

func Solve(p Problem) int {
	total := 0
	for i := 0; i < len(p.InternshipDays)-1; i++ {
		end := p.InternshipDays[i].End
		begin := p.InternshipDays[i+1].Begin
		duration := begin - end
		expressFee := 2 * p.ExpressFee
		hotelFee := duration * p.HotelFee
		total += min(expressFee, hotelFee)
	}
	return total + 2*p.ExpressFee
}

func min(x, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}
