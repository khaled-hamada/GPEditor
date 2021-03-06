// Generated by gencpp from file baymax_msgs/baymaxPose.msg
// DO NOT EDIT!


#ifndef BAYMAX_MSGS_MESSAGE_BAYMAXPOSE_H
#define BAYMAX_MSGS_MESSAGE_BAYMAXPOSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace baymax_msgs
{
template <class ContainerAllocator>
struct baymaxPose_
{
  typedef baymaxPose_<ContainerAllocator> Type;

  baymaxPose_()
    : x(0.0)
    , y(0.0)
    , theta(0.0)  {
    }
  baymaxPose_(const ContainerAllocator& _alloc)
    : x(0.0)
    , y(0.0)
    , theta(0.0)  {
  (void)_alloc;
    }



   typedef float _x_type;
  _x_type x;

   typedef float _y_type;
  _y_type y;

   typedef float _theta_type;
  _theta_type theta;





  typedef boost::shared_ptr< ::baymax_msgs::baymaxPose_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::baymax_msgs::baymaxPose_<ContainerAllocator> const> ConstPtr;

}; // struct baymaxPose_

typedef ::baymax_msgs::baymaxPose_<std::allocator<void> > baymaxPose;

typedef boost::shared_ptr< ::baymax_msgs::baymaxPose > baymaxPosePtr;
typedef boost::shared_ptr< ::baymax_msgs::baymaxPose const> baymaxPoseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::baymax_msgs::baymaxPose_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::baymax_msgs::baymaxPose_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace baymax_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'baymax_msgs': ['/home/khaled/baymax_ws2/src/baymax_msgs/msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::baymax_msgs::baymaxPose_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::baymax_msgs::baymaxPose_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::baymax_msgs::baymaxPose_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::baymax_msgs::baymaxPose_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::baymax_msgs::baymaxPose_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::baymax_msgs::baymaxPose_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::baymax_msgs::baymaxPose_<ContainerAllocator> >
{
  static const char* value()
  {
    return "a130bc60ee6513855dc62ea83fcc5b20";
  }

  static const char* value(const ::baymax_msgs::baymaxPose_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xa130bc60ee651385ULL;
  static const uint64_t static_value2 = 0x5dc62ea83fcc5b20ULL;
};

template<class ContainerAllocator>
struct DataType< ::baymax_msgs::baymaxPose_<ContainerAllocator> >
{
  static const char* value()
  {
    return "baymax_msgs/baymaxPose";
  }

  static const char* value(const ::baymax_msgs::baymaxPose_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::baymax_msgs::baymaxPose_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
float32 x\n\
float32 y\n\
float32 theta\n\
";
  }

  static const char* value(const ::baymax_msgs::baymaxPose_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::baymax_msgs::baymaxPose_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.theta);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct baymaxPose_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::baymax_msgs::baymaxPose_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::baymax_msgs::baymaxPose_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<float>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<float>::stream(s, indent + "  ", v.y);
    s << indent << "theta: ";
    Printer<float>::stream(s, indent + "  ", v.theta);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BAYMAX_MSGS_MESSAGE_BAYMAXPOSE_H
