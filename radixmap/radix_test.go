package radixmap

import (
	"testing"
)

func TestRadix(t *testing.T) {
	r := New()
	key := []byte("test")
	r.Add(key, 1)

	val, ok := r.Get(key)
	t.Logf("%s %d %t", key, val, ok)

	key = []byte("test123")

	key, val, ok = r.LongestPrefix(key)
	t.Logf("%s %d %t", key, val, ok)

	r.WalkPrefix([]byte("t"), func(s []byte, v interface{}) bool {
		t.Logf("%s %d", s, v)
		return true
	})
}
