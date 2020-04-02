/*
--------------------------------------------------
 File Name: main.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-19-下午6:27
---------------------说明--------------------------

--------------------------------------------------
*/

package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
)

func recursiveDir(bfilelist []*os.FileInfo, fileDir os.FileInfo) ([]*os.FileInfo) {
	if fileDir.IsDir() {
		
		if filelist, err := ioutil.ReadDir(fileDir.Name()); err == nil {
			for itemindex := range filelist {
				fileitem := filelist[itemindex]
				if fileitem.IsDir() {
					bfilelist = recursiveDir(bfilelist, fileitem)
					
				} else {
					bfilelist = append(bfilelist, &fileitem)
				}
			}
		}
	}
	return bfilelist
}

func filepathwalk() {
	dir := "dir/to/walk"
	subDirToSkip := "skip" // dir/to/walk/skip
	
	err := filepath.Walk(dir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			fmt.Printf("prevent panic by handling failure accessing a path %q: %v\n", dir, err)
			return err
		}
		if info.IsDir() && info.Name() == subDirToSkip {
			fmt.Printf("skipping a dir without errors: %+v \n", info.Name())
			return filepath.SkipDir
		}
		fmt.Printf("visited file: %q\n", path)
		return nil
	})
	
	if err != nil {
		fmt.Printf("error walking the path %q: %v\n", dir, err)
	}
}

func main() {
	dirpath := "/data/"
	// filelist := path.Dir(dirpath)
	// fileinfo, _ := os.Open(dirpath)
	if err := filepath.Walk(dirpath, func(path string, info os.FileInfo, err error) error {
		
		fmt.Printf("%v-[%v] \n", path, info)
		return err
	}); err != nil {
		fmt.Printf("error")
	}
	
	// bfilelist := []*os.FileInfo{}
	// recursiveDir(bfilelist, os.FileInfo(fileinfo))
}
