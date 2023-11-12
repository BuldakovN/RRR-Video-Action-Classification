package entity
//структуры для работы
type Form struct{
	USER string `json:"user" binding:"required"`
    PASSWORD string `json:"password" binding:"required"`
}

type FormBase64 struct{
	TYPE string `json:"type" binding:"required"`
	BASE64 string `json:"b64" binding:"required"`
	VIDEONAME string `json:"name" binding:"required"`
}

type FormBase64Double struct{
	TYPE string `json:"type" binding:"required"`
	BASE64 string `json:"b64" binding:"required"`
	TYPET string `json:"typet" binding:"required"`
	BASE64T string `json:"b64t" binding:"required"`
}

