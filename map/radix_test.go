package radix

import (
	"testing"
)

func TestRadix(t *testing.T) {
	r:=New()
	key := []byte("test")
	r.Insert(key,1)
	val, ok := r.Get(key)

	t.Logf("%d %t", val, ok)

}