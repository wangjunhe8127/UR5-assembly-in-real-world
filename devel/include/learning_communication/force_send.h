// Generated by gencpp from file learning_communication/force_send.msg
// DO NOT EDIT!


#ifndef LEARNING_COMMUNICATION_MESSAGE_FORCE_SEND_H
#define LEARNING_COMMUNICATION_MESSAGE_FORCE_SEND_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace learning_communication
{
template <class ContainerAllocator>
struct force_send_
{
  typedef force_send_<ContainerAllocator> Type;

  force_send_()
    : fx(0.0)
    , fy(0.0)
    , fz(0.0)
    , tx(0.0)
    , ty(0.0)
    , tz(0.0)  {
    }
  force_send_(const ContainerAllocator& _alloc)
    : fx(0.0)
    , fy(0.0)
    , fz(0.0)
    , tx(0.0)
    , ty(0.0)
    , tz(0.0)  {
  (void)_alloc;
    }



   typedef double _fx_type;
  _fx_type fx;

   typedef double _fy_type;
  _fy_type fy;

   typedef double _fz_type;
  _fz_type fz;

   typedef double _tx_type;
  _tx_type tx;

   typedef double _ty_type;
  _ty_type ty;

   typedef double _tz_type;
  _tz_type tz;





  typedef boost::shared_ptr< ::learning_communication::force_send_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::learning_communication::force_send_<ContainerAllocator> const> ConstPtr;

}; // struct force_send_

typedef ::learning_communication::force_send_<std::allocator<void> > force_send;

typedef boost::shared_ptr< ::learning_communication::force_send > force_sendPtr;
typedef boost::shared_ptr< ::learning_communication::force_send const> force_sendConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::learning_communication::force_send_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::learning_communication::force_send_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace learning_communication

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'learning_communication': ['/home/xsm/control/src/learning_communication/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::learning_communication::force_send_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::learning_communication::force_send_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::learning_communication::force_send_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::learning_communication::force_send_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::learning_communication::force_send_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::learning_communication::force_send_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::learning_communication::force_send_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e6da1f4bb463d64b2399f31589512a6f";
  }

  static const char* value(const ::learning_communication::force_send_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe6da1f4bb463d64bULL;
  static const uint64_t static_value2 = 0x2399f31589512a6fULL;
};

template<class ContainerAllocator>
struct DataType< ::learning_communication::force_send_<ContainerAllocator> >
{
  static const char* value()
  {
    return "learning_communication/force_send";
  }

  static const char* value(const ::learning_communication::force_send_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::learning_communication::force_send_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 fx\n\
float64 fy\n\
float64 fz\n\
float64 tx\n\
float64 ty\n\
float64 tz\n\
\n\
";
  }

  static const char* value(const ::learning_communication::force_send_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::learning_communication::force_send_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.fx);
      stream.next(m.fy);
      stream.next(m.fz);
      stream.next(m.tx);
      stream.next(m.ty);
      stream.next(m.tz);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct force_send_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::learning_communication::force_send_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::learning_communication::force_send_<ContainerAllocator>& v)
  {
    s << indent << "fx: ";
    Printer<double>::stream(s, indent + "  ", v.fx);
    s << indent << "fy: ";
    Printer<double>::stream(s, indent + "  ", v.fy);
    s << indent << "fz: ";
    Printer<double>::stream(s, indent + "  ", v.fz);
    s << indent << "tx: ";
    Printer<double>::stream(s, indent + "  ", v.tx);
    s << indent << "ty: ";
    Printer<double>::stream(s, indent + "  ", v.ty);
    s << indent << "tz: ";
    Printer<double>::stream(s, indent + "  ", v.tz);
  }
};

} // namespace message_operations
} // namespace ros

#endif // LEARNING_COMMUNICATION_MESSAGE_FORCE_SEND_H
