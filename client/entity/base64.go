package entity

import (
	"encoding/base64"
	"log"
	"os"
)



func Base64ToFile(b64 string) {
    log.Println("декодируем строку")
    dec, err := base64.StdEncoding.DecodeString(b64)
    if err != nil {
        panic(err)
    }
    log.Println("сохраянем файл")
    f, err := os.Create("videos/out.avi")
    if err != nil {
        panic(err)
    }
    defer f.Close()

    if _, err := f.Write(dec); err != nil {
        panic(err)
    }
    if err := f.Sync(); err != nil {
        panic(err)
    }
}