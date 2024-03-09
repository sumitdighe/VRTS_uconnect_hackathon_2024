\package driver_test

import (
	"testing"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

func TestS3Driver(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "S3Driver")
}
