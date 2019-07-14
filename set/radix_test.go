package radix

import (
	"testing"
)

func TestRadix(t *testing.T) {
	r:=New()
	key := []byte("test")
	r.Add(key)

	ok := r.Get(key)
	t.Logf("%s %t", key,  ok)

	key = []byte("test123")

	key,  ok = r.LongestPrefix(key)
	t.Logf("%s %t", key, ok)

	r.WalkPrefix([]byte("t"), func(s []byte) bool {
		t.Logf("%s", s)
		return true
	})
	r.Add([]byte("t2"))
	t.Logf("len %d",r.Len())
}