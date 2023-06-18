package setubunrobot

type Turn struct {
	Left  uint
	Right uint
	Count uint
}

type Problem struct {
	Members []uint
	Turns   []Turn
}

type Answer struct {
	Beans []uint
}

type Distributer interface {
	Distribute(p Problem) Answer
}

func New() Distributer {
	return &distributerImpl{}
}

type distributerImpl struct{}

func (d *distributerImpl) Distribute(p Problem) Answer {
	beans := make([]uint, len(p.Members))
	for _, turn := range p.Turns {
		for i := turn.Left; i <= turn.Right; i++ {
			beans[i] += turn.Count
			if p.Members[i] < beans[i] {
				beans[i] = p.Members[i]
			}
		}
	}
	return Answer{Beans: beans}
}
