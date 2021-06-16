# C++ Notes

`i++;` or `++i;` are same by themselves but it differs if more expressions involve.

E.g. 
`a = 0`

`int a = i++;`

string could be AD

std::string is an implementation

## Class

Constructor to initialize the attributes.

`Square(int side): area(side**2), perimeter(side*4)`



## Template

### Template Class

**ADVISE: Make a non-template class and test thoroughly, then convert it to template class. Don't write the template class straightt.**

You need to write template class in the same header file. Don't split into cpp file.

Template 
myHeder.h
```
template <class T>
class myClass
{
    private:
    T data;
    Node<T> * top;
}

```

Method examples (myHeader.h, on the same file):

```
template <class T>
void myClass<T>::mymethod() {}

template <class T>
myClass<T> myClass<T>::mymethod(T value) {}

template <class T>
T myClass<T>::mymethod(T value) {}

template <class T>
myClass<T> myClass<T>::operator=(const T & obj) {}
```