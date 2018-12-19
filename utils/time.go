package utils

import (
	"fmt"
	"strconv"
	"time"
)

func TimeStringToString(str string) (string, error) {
	if st, err := time.Parse("2006-01-02", str); nil == err {
		return st.Format("20060102"), err
	} else {
		return "", err
	}
}

func TimeStringToInt(str string) int {
	if str1, err := TimeStringToString(str); nil == err {
		if tint, err := strconv.Atoi(str1); nil == err {
			return tint
		} else {
			return 0
		}
	} else {
		return 0
	}
}

func TimeStringRangeToInt(str1 string, str2 string) []int {
	timetmp := []int{}
	day1, _ := time.ParseDuration("24h")
	tm, _ := time.ParseInLocation("2006-01-02", str1, time.Local)
	for t1 := TimeStringToInt(str1); t1 <= TimeStringToInt(str2); {
		tmInt1, _ := strconv.Atoi(tm.Format("20060102"))
		timetmp = append(timetmp, tmInt1)
		tm = tm.Add(day1)
		t1 = TimeStringToInt(tm.Format("2006-01-02"))
	}
	return timetmp
}

func TimeIntToString(it int) string {
	if st, err := time.Parse("20060102", strconv.Itoa(it)); nil == err {
		return st.Format("2006-01-02")
	} else {
		// 错误
		fmt.Println("错误")
		return ""
	}
}
