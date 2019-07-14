package main

import (
	"github.com/u6du/radix/radixmap"
	"github.com/u6du/radix/radixset"
)

func NewMap() *radixmap.Tree {
	return radixmap.New()
}

func NewSet() *radixset.Tree {
	return radixset.New()
}
