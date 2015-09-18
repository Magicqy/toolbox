#!/usr/bin/python
import os, sys, argparse, xml.etree.ElementTree

def ModifyMetaData(srcFile, dstFile, newValues):
    ns = 'http://schemas.android.com/apk/res/android'
    fname, fvalue = '{%s}name' %ns, '{%s}value' %ns

    xml.etree.ElementTree.register_namespace('android', ns)
    xmltree = xml.etree.ElementTree.parse(srcFile)
    appNode = xmltree.find('application')
    if appNode != None:
        allmd = appNode.findall('meta-data')
        for md in allmd:
            name, value = md.get(fname), md.get(fvalue)
            if name in newValues:
                md.set(fvalue, newValues[name])
                print('name="%s" (value="%s") => (value="%s")' %(name, value, newValues[name]))
    else:
        print('application node not found, invalid AndroidManifest.xml')
    
    xmltree.write(dstFile, 'utf-8', True)
    print('modify finished')
pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'AndroidManifest meta data modifier')
    parser.add_argument('srcFile', help = 'source xml file')
    parser.add_argument('dstFile', help = 'new xml file to save')
    parser.add_argument('-md', nargs = 2, action = 'append', required = True,
                        help = 'meta-data name/value pair to modify')
    args = parser.parse_args()

    if args.md and len(args.md) > 0:
        newValues = {}
        for item in args.md:
            newValues[item[0]] = item[1]
        ModifyMetaData(args.srcFile, args.dstFile, newValues)
    pass
